#!/bin/bash
set -e

host="$DB_HOST"
port="3306"

echo "Aguardando banco de dados em $host:$port..."

until nc -z "$host" "$port"; do
  echo "Banco de dados ainda não está pronto..."
  sleep 2
done

echo "Banco de dados está pronto! Iniciando a aplicação..."

exec "$@"
