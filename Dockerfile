FROM python:3.8-slim-buster AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev libjpeg-dev vim && \
    apt-get install -y python3-pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

RUN ["chmod", "+x", "server_start.sh"]

ENTRYPOINT ["sh","./server_start.sh"]

