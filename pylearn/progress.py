"""SQLite-backed progress tracking."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ProgressDB:
    """Track exercise completion, scores, and streaks."""

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or Path.home() / ".pylearn" / "progress.db"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self) -> None:
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                exercise_id TEXT NOT NULL,
                topic TEXT NOT NULL,
                passed INTEGER NOT NULL,
                score_pct INTEGER NOT NULL,
                attempted_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS completions (
                exercise_id TEXT PRIMARY KEY,
                topic TEXT NOT NULL,
                best_score INTEGER NOT NULL DEFAULT 0,
                attempts INTEGER NOT NULL DEFAULT 0,
                first_completed_at TEXT,
                last_attempted_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS streaks (
                date TEXT PRIMARY KEY,
                exercises_done INTEGER NOT NULL DEFAULT 0
            );
        """)
        self.conn.commit()

    def record_attempt(self, exercise_id: str, topic: str, passed: bool, score_pct: int) -> None:
        now = datetime.now(timezone.utc).isoformat()

        self.conn.execute(
            "INSERT INTO attempts (exercise_id, topic, passed, score_pct, attempted_at) VALUES (?, ?, ?, ?, ?)",
            (exercise_id, topic, int(passed), score_pct, now),
        )

        existing = self.conn.execute(
            "SELECT * FROM completions WHERE exercise_id = ?", (exercise_id,)
        ).fetchone()

        if existing:
            self.conn.execute(
                """UPDATE completions SET
                    best_score = MAX(best_score, ?),
                    attempts = attempts + 1,
                    first_completed_at = CASE WHEN ? = 1 AND first_completed_at IS NULL THEN ? ELSE first_completed_at END,
                    last_attempted_at = ?
                WHERE exercise_id = ?""",
                (score_pct, int(passed), now, now, exercise_id),
            )
        else:
            self.conn.execute(
                """INSERT INTO completions (exercise_id, topic, best_score, attempts, first_completed_at, last_attempted_at)
                VALUES (?, ?, ?, 1, ?, ?)""",
                (exercise_id, topic, score_pct, now if passed else None, now),
            )

        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.conn.execute(
            """INSERT INTO streaks (date, exercises_done) VALUES (?, 1)
            ON CONFLICT(date) DO UPDATE SET exercises_done = exercises_done + 1""",
            (today,),
        )

        self.conn.commit()

    def get_topic_stats(self, topic: str) -> dict[str, Any]:
        row = self.conn.execute(
            """SELECT
                COUNT(*) as attempted,
                SUM(CASE WHEN best_score = 100 THEN 1 ELSE 0 END) as completed,
                AVG(best_score) as avg_score
            FROM completions WHERE topic = ?""",
            (topic,),
        ).fetchone()
        return dict(row) if row else {"attempted": 0, "completed": 0, "avg_score": 0}

    def get_all_stats(self) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            """SELECT topic,
                COUNT(*) as attempted,
                SUM(CASE WHEN best_score = 100 THEN 1 ELSE 0 END) as completed,
                ROUND(AVG(best_score), 1) as avg_score
            FROM completions GROUP BY topic ORDER BY topic"""
        ).fetchall()
        return [dict(r) for r in rows]

    def get_streak(self) -> int:
        rows = self.conn.execute(
            "SELECT date FROM streaks ORDER BY date DESC LIMIT 30"
        ).fetchall()
        if not rows:
            return 0
        streak = 0
        today = datetime.now(timezone.utc).date()
        for row in rows:
            expected = today - __import__("datetime").timedelta(days=streak)
            if row["date"] == expected.isoformat():
                streak += 1
            else:
                break
        return streak

    def is_completed(self, exercise_id: str) -> bool:
        row = self.conn.execute(
            "SELECT best_score FROM completions WHERE exercise_id = ?", (exercise_id,)
        ).fetchone()
        return row is not None and row["best_score"] == 100

    def get_total_completed(self) -> int:
        row = self.conn.execute(
            "SELECT COUNT(*) as n FROM completions WHERE best_score = 100"
        ).fetchone()
        return row["n"] if row else 0

    def close(self) -> None:
        self.conn.close()
