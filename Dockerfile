from pypy:3-slim

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install tornado
RUN pip install kafka-python
