FROM python:3.11-slim

WORKDIR /app

# Install system deps (for building Python packages cleanly)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app (main.py has "app")
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
