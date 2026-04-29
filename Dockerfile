FROM python:3.11-alpine
RUN apk update && apk upgrade --no-cache
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache gcc musl-dev libpq-dev && \
    pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
