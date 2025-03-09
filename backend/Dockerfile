FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY scripts/wait-for-db.sh /app/scripts/wait-for-db.sh

RUN chmod +x /app/scripts/wait-for-db.sh

ENTRYPOINT ["sh", "/app/scripts/wait-for-db.sh"]

CMD ["fastapi", "run", "app/main.py"]
