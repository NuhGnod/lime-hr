FROM python:3.8-slim-buster AS builder

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev libjpeg-dev vim && \
    apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install django-debug-toolbar

# FROM python:3.8-slim-buster
# COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
# WORKDIR /djangoproject

ENV PYTHONUNBUFFERED=1
COPY server_start.sh /

COPY . /app
RUN chmod +x /server_start.sh
