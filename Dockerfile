FROM python:3.11-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "until nc -z sge_db 5432; do sleep 1; done; python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]