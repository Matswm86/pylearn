"""Interactive CLI for PyLearn."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table
from rich.text import Text
from rich import box

from .exercises.base import Difficulty, Exercise
from .progress import ProgressDB
from .runner import grade_exercise, load_user_solution, save_starter_code

console = Console()

TOPICS = {
    "1": ("variables", "Variables"),
    "2": ("data_types", "Data Types"),
    "3": ("conditionals", "Conditionals (if/else)"),
    "4": ("functions", "Functions"),
    "5": ("lists_sets", "Lists & Sets"),
    "6": ("dictionaries", "Dictionaries"),
    "7": ("fastapi_ex", "FastAPI"),
    "8": ("api_calling", "API Calling"),
}


def get_all_exercises() -> dict[str, list[Exercise]]:
    """Load all exercise modules."""
    from .exercises import (
        variables,
        data_types,
        conditionals,
        functions,
        lists_sets,
        dictionaries,
        fastapi_ex,
        api_calling,
    )

    return {
        "variables": variables.exercises,
        "data_types": data_types.exercises,
        "conditionals": conditionals.exercises,
        "functions": functions.exercises,
        "lists_sets": lists_sets.exercises,
        "dictionaries": dictionaries.exercises,
        "fastapi_ex": fastapi_ex.exercises,
        "api_calling": api_calling.exercises,
    }


def show_banner(db: ProgressDB) -> None:
    total = db.get_total_completed()
    streak = db.get_streak()
    banner = Text()
    banner.append("PyLearn", style="bold cyan")
    banner.append(" - Interactive Python Trainer\n", style="dim")
    banner.append(f"Completed: {total}/400", style="green")
    banner.append(f"  |  Streak: {streak} day{'s' if streak != 1 else ''}", style="yellow")
    console.print(Panel(banner, box=box.ROUNDED))


def show_topic_menu(db: ProgressDB, all_exercises: dict[str, list[Exercise]]) -> None:
    table = Table(title="Topics", box=box.SIMPLE_HEAVY)
    table.add_column("#", style="cyan", width=3)
    table.add_column("Topic", style="bold")
    table.add_column("Progress", justify="right")
    table.add_column("Completed", justify="right", style="green")

    for key, (module, label) in TOPICS.items():
        exercises = all_exercises.get(module, [])
        total = len(exercises)
        stats = db.get_topic_stats(module)
        completed = int(stats.get("completed", 0) or 0)
        pct = int(completed / total * 100) if total > 0 else 0
        bar_len = 20
        filled = int(pct / 100 * bar_len)
        bar = f"[green]{'█' * filled}[/green][dim]{'░' * (bar_len - filled)}[/dim]"
        table.add_row(key, label, bar, f"{completed}/{total}")

    console.print(table)
    console.print("[dim]  0. Quit[/dim]")


def show_exercise_list(exercises: list[Exercise], db: ProgressDB, topic_label: str) -> None:
    table = Table(title=f"{topic_label} Exercises", box=box.SIMPLE)
    table.add_column("#", style="cyan", width=4)
    table.add_column("Title", style="bold", max_width=50)
    table.add_column("Difficulty", width=12)
    table.add_column("Status", width=8, justify="center")

    for i, ex in enumerate(exercises, 1):
        done = db.is_completed(ex.id)
        status = "[green]PASS[/green]" if done else "[dim]--[/dim]"
        diff_colors = {1: "green", 2: "cyan", 3: "yellow", 4: "red", 5: "bold red"}
        color = diff_colors.get(ex.difficulty.value, "white")
        table.add_row(str(i), ex.title, f"[{color}]{ex.difficulty}[/{color}]", status)

    console.print(table)
    console.print("[dim]  0. Back to topics[/dim]")


def show_exercise(exercise: Exercise, workspace: Path) -> None:
    panel_content = exercise.description
    if exercise.concepts:
        panel_content += f"\n\n[dim]Concepts: {', '.join(exercise.concepts)}[/dim]"

    console.print(Panel(
        panel_content,
        title=f"[bold]{exercise.title}[/bold]  [{exercise.difficulty}]",
        border_style="cyan",
    ))

    if exercise.function_name and exercise.test_cases:
        console.print(f"\n[bold]Function signature:[/bold] def {exercise.function_name}(...)")
        shown = exercise.test_cases[:3]
        for tc in shown:
            console.print(f"  {exercise.function_name}{tc.input_args} -> {tc.expected!r}")

    solution_file = save_starter_code(exercise, workspace)
    console.print(f"\n[dim]Solution file: {solution_file}[/dim]")


def run_exercise(exercise: Exercise, workspace: Path, db: ProgressDB) -> None:
    show_exercise(exercise, workspace)

    while True:
        console.print("\n[bold]Commands:[/bold] [cyan]c[/cyan]heck | [cyan]h[/cyan]int | [cyan]s[/cyan]olution | [cyan]e[/cyan]dit | [cyan]b[/cyan]ack")
        cmd = Prompt.ask("", default="c").strip().lower()

        if cmd in ("b", "back", "q"):
            break
        elif cmd in ("h", "hint"):
            if exercise.hints:
                hint_idx = getattr(exercise, "_hint_idx", 0)
                if hint_idx < len(exercise.hints):
                    console.print(f"\n[yellow]Hint {hint_idx + 1}/{len(exercise.hints)}:[/yellow] {exercise.hints[hint_idx]}")
                    exercise._hint_idx = hint_idx + 1
                else:
                    console.print("[dim]No more hints.[/dim]")
            else:
                console.print("[dim]No hints available.[/dim]")
        elif cmd in ("s", "solution", "sol"):
            if exercise.solution:
                console.print(Panel(exercise.solution, title="Solution", border_style="green"))
            else:
                console.print("[dim]No solution available.[/dim]")
        elif cmd in ("e", "edit"):
            solution_file = save_starter_code(exercise, workspace)
            editor = "code" if _command_exists("code") else "nano"
            subprocess.run([editor, str(solution_file)])
        elif cmd in ("c", "check", ""):
            user_code = load_user_solution(exercise.id, workspace)
            if user_code is None:
                console.print("[red]No solution file found. Press 'e' to edit.[/red]")
                continue

            result = grade_exercise(exercise, user_code)

            if result.passed:
                console.print(f"\n[bold green]PASSED![/bold green] ({result.passed_tests}/{result.total_tests} tests)")
                db.record_attempt(exercise.id, exercise.topic, True, result.score_pct)
            else:
                console.print(f"\n[bold red]FAILED[/bold red] ({result.passed_tests}/{result.total_tests} tests)")
                for err in result.errors[:5]:
                    console.print(f"  [red]{err}[/red]")
                db.record_attempt(exercise.id, exercise.topic, False, result.score_pct)

            if result.output:
                console.print(f"\n[dim]Output:[/dim]\n{result.output.rstrip()}")


def _command_exists(cmd: str) -> bool:
    from shutil import which
    return which(cmd) is not None


def main() -> None:
    workspace = Path.cwd() / "solutions"
    workspace.mkdir(exist_ok=True)
    db = ProgressDB()

    try:
        all_exercises = get_all_exercises()
    except ImportError as e:
        console.print(f"[red]Failed to load exercises: {e}[/red]")
        sys.exit(1)

    while True:
        console.clear()
        show_banner(db)
        show_topic_menu(db, all_exercises)

        choice = Prompt.ask("\nSelect topic", default="0")
        if choice == "0":
            console.print("[dim]Goodbye![/dim]")
            break

        if choice not in TOPICS:
            continue

        module_name, topic_label = TOPICS[choice]
        exercises = all_exercises.get(module_name, [])

        while True:
            console.clear()
            show_exercise_list(exercises, db, topic_label)

            ex_choice = Prompt.ask("\nSelect exercise", default="0")
            if ex_choice == "0":
                break

            try:
                idx = int(ex_choice) - 1
                if 0 <= idx < len(exercises):
                    run_exercise(exercises[idx], workspace, db)
                else:
                    console.print("[red]Invalid number.[/red]")
            except ValueError:
                console.print("[red]Enter a number.[/red]")

    db.close()


if __name__ == "__main__":
    main()
