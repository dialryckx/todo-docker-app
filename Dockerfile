FROM python:3.10-slim
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
WORKDIR /todo-app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD redis-server --daemonize yes && uvicorn main:app --host 0.0.0.0 --port 8000  
