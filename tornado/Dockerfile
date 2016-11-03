from pypy:3-slim

RUN apt-get update &&  apt-get install -y \
        libpq-dev \
        clang

RUN pip install tornado
RUN pip install kafka-python
RUN pip install motor
RUN pip install elasticsearch
RUN pip install couchdb
RUN pip install pika
RUN pip install psycopg2cffi
RUN pip install cassandra-driver

RUN mkdir /app
WORKDIR /app
COPY . /app
