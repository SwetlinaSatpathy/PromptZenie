#!/bin/bash
set -e

# Start Ollama in background
ollama serve &

# Use Render-provided PORT or default 8080
PORT=${PORT:-8080}

# Start FastAPI server
uvicorn server:app --host 0.0.0.0 --port $PORT
