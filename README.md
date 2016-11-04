# Python tornado practice project

The purpose of this project is to experiment with tornado
and also learn general python api connections to popular databases.
I did some benchmarks but like all benchmarks they don't give a full story.

## Benchmarks in requests/sec (timeouts)

`wrk -t 100 -c 500 -s wrk.lua http://localhost:4000/rabbitmq/async`

| TARGET | SYNC  | ASYNC(via thread executor)  | ASYNC(via single thread)
|---|---|---|---|
| rabbitmq  | 2279 (86)  | 1121 (1) | |
| kafka  | 1510 ( 156)  | 941 (9) | |
| mongodb  |   |   |913 (10) |
| cassandra  |   |   | |
| elasticsearch  |   |   | |
| postgres-json | | | |
| postgres-jsonb | | | |
| postgres-text | 232 | 253 | | 

## Conclusions
It is not surprising that the sync code cameout faster than async. 
Since the goal of async isn't speed but number of connections. 
Of course there are a lot more timeouts when working with sync code.

## Goals
* ~~Use tornado to accept JSON and write to target storage~~
* ~~Use docker~~
* JSON to cassandra
* ~~JSON to kafka~~
* ~~JSON to postgresql~~
* ~~JSON to mongodb~~
* ~~JSON to couchdb~~
* ~~JSON to elastic search~~
* JSON to logstash
* ~~JSON to rabbitmq~~
* Visualization software of all of the above(if it exists)
* Make all at least concurrent.. but determine which can be single threaded async and not.. and why
* Simple benchmarks of sync(if created) and async of each


## Extra goals - depends on how long the above takes
* ~~Compare using tornado async libraries vers python3 concurrent~~





