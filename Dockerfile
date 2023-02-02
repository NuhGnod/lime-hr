FROM python:3.8-slim-buster AS builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev libjpeg-dev vim && \
    apt-get install -y python3-pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install django-debug-toolbar

COPY ./server_start.sh /usr/src/app/server_start.sh

COPY . /usr/src/app/

RUN chmod 755 /usr/src/app/server_start.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

