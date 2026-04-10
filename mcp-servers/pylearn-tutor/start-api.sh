#!/bin/bash
# Start the PyLearn Tutor HTTP API bridge
# Requires: pip install -r requirements.txt && ollama serve
cd "$(dirname "$0")"
exec uvicorn api_bridge:app --host 127.0.0.1 --port 8000
