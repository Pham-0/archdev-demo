FROM python:3.12-slim

WORKDIR /app

# Cài FastAPI + Uvicorn
RUN pip install fastapi uvicorn

COPY . /app

# Chạy FastAPI bằng Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

