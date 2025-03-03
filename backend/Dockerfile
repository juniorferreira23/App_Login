FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for-db.sh /app/wait-for-db.sh

RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000

CMD ["/app/wait-for-db.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
