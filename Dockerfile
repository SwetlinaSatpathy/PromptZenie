# Use lightweight Python image
FROM python:3.11-slim

# Install curl for Ollama
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://ollama.com/download/ollama-linux-amd64.tgz -o ollama.tgz && \
    tar -xzf ollama.tgz && mv ollama /usr/local/bin/ollama && \
    rm ollama.tgz

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optional: pull the model during build to speed up deploy
RUN ollama pull phi3:mini

# Expose Render default port (optional)
EXPOSE 8080

# Run start.sh as the main command
CMD ["bash", "start.sh"]
