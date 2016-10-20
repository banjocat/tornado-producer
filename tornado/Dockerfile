from pypy:3-slim

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN apt-get update
# for postgres
RUN apt-get install -y libpq-dev clang

RUN pip install tornado
RUN pip install kafka-python
RUN pip install motor
RUN pip install elasticsearch
RUN pip install couchdb
RUN pip install pika
RUN pip install psycopg2cffi
