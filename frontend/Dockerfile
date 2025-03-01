# frontend/Dockerfile
FROM node:22.14.0-slim

WORKDIR /app

COPY . .

RUN npm install
RUN npm install -g http-server

EXPOSE 8080

CMD ["http-server", ".", "-p", "8080"]