#!/bin/bash
set -e

host="$DB_HOST"
port="3306"

echo "Aguardando banco de dados em $host:$port..."

while ! timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null; do
  echo "Banco de dados ainda não está pronto..."
  sleep 2
done

echo "Banco de dados está pronto! Iniciando a aplicação..."

exec "$@"
