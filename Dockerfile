FROM python:3.8-slim-buster AS builder

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev libjpeg-dev vim && \
    apt-get install -y python3-pip

WORKDIR /lime_hrm

COPY requirements.txt /lime_hrm

RUN pip install -r requirements.txt
RUN pip install django-debug-toolbar

# FROM python:3.8-slim-buster
# COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
# WORKDIR /djangoproject

COPY . /lime_hrm

ENV PYTHONUNBUFFERED=1

CMD gunicorn \
    --workers=1 \
    --timeout=1800 \
    --access-logfile - \
    --log-level - \
    --error-logfile - \
    config.wsgi:application \

    --bind 0.0.0.0:8000 \

    --max-requests 1000 \

    --max-requests-jitter 50
