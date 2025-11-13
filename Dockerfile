FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://ollama.com/install.sh | bash

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["./start.sh"]
