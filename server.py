from fastapi import FastAPI, Request
import subprocess
import json

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    result = subprocess.run(
        ["ollama", "run", "phi3:mini", prompt],
        stdout=subprocess.PIPE,
        text=True
    )
    return {"response": result.stdout.strip()}
