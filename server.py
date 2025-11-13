import os
from fastapi import FastAPI, Request
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PromptZenie API")

# CORS for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for Render health checks
@app.get("/")
def root():
    return {"status": "ok"}

# Generate structured response
@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "No prompt provided"}

    try:
        result = subprocess.run(
            ["ollama", "run", "phi3:mini", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return {"error": "Ollama failed", "details": result.stderr}
        return {"response": result.stdout.strip()}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
