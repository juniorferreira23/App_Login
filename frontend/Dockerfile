# frontend/Dockerfile
FROM node:22.14.0-slim

WORKDIR /app

COPY . .

RUN npm install
RUN npm install -g http-server

EXPOSE 3000

CMD ["http-server", ".", "-p", "3000"]