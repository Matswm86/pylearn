#!/bin/bash
# PyLearn Tutor MCP Server Startup Script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}PyLearn Tutor MCP Server${NC}"
echo "=========================="
echo ""

# Check Python
echo -n "Checking Python... "
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}FAILED${NC}"
    echo "Python 3 not found. Please install Python 3.11+"
    exit 1
fi
PY_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}OK${NC} (Python $PY_VERSION)"

# Check dependencies
echo -n "Checking dependencies... "
if ! python3 -c "import fastmcp" 2>/dev/null; then
    echo -e "${YELLOW}MISSING${NC}"
    echo "Installing dependencies..."
    pip install -q -r "$SCRIPT_DIR/requirements.txt"
    echo -e "${GREEN}Installed${NC}"
else
    echo -e "${GREEN}OK${NC}"
fi

# Check Ollama
echo -n "Checking Ollama connection... "
OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
if curl -s "$OLLAMA_URL/api/tags" > /dev/null 2>&1; then
    echo -e "${GREEN}OK${NC}"
else
    echo -e "${YELLOW}FAILED${NC}"
    echo -e "${YELLOW}Warning: Ollama is not responding at $OLLAMA_URL${NC}"
    echo "Make sure Ollama is running: ollama serve"
    echo ""
fi

# Check exercises.json
echo -n "Checking exercises.json... "
EXERCISES_PATH="${PYLEARN_EXERCISES_PATH:-$SCRIPT_DIR/../../../docs/exercises.json}"
if [ -f "$EXERCISES_PATH" ]; then
    EXERCISE_COUNT=$(python3 -c "import json; print(json.load(open('$EXERCISES_PATH')).get('total_exercises', '?'))")
    echo -e "${GREEN}OK${NC} ($EXERCISE_COUNT exercises)"
else
    echo -e "${YELLOW}NOT FOUND${NC}"
    echo "Exercises path: $EXERCISES_PATH"
fi

echo ""
echo -e "${GREEN}Starting server...${NC}"
echo "Environment:"
echo "  OLLAMA_URL: ${OLLAMA_URL:-http://localhost:11434}"
echo "  OLLAMA_MODEL: ${OLLAMA_MODEL:-llama3.2:3b}"
echo "  PYTHONUNBUFFERED: 1"
echo ""

# Export environment variables
export PYTHONUNBUFFERED=1
export OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
export OLLAMA_MODEL="${OLLAMA_MODEL:-llama3.2:3b}"

# Start server
cd "$SCRIPT_DIR"
python3 server.py
