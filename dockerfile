FROM python:3.9-slim

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7999

CMD [ "python", "backend/server.py" ]
