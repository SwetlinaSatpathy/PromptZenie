#!/bin/bash
ollama serve &
sleep 5
ollama pull phi3:mini
uvicorn server:app --host 0.0.0.0 --port 8080
