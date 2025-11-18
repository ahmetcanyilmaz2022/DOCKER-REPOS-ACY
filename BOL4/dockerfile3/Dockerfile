# ------------------------
# 1. Build Stage
# ------------------------
FROM node:18 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# ------------------------
# 2. Production Stage
# ------------------------
FROM node:18-slim

WORKDIR /app
COPY --from=builder /app ./

ENV PORT=4000
EXPOSE 4000

CMD ["node", "src/index.js"]