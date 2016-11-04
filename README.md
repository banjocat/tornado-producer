#### In development

# Python tornado practice project

The purpose of this project is to experiment with tornado
and also learn general python api connections to popular databases.

# Benchmarks in requests/sec

| TARGET | SYNC  | ASYNC(via executor)  | ASYNC(via single thread)
|---|---|---|---|
| rabbitmq  | 2018  | 1121  | |
| kafka  | 1339  | 941  | |
| mongodb  |   |   |913 |
| cassandra  |   |   | |
| elasticsearch  |   |   | |
| postgres-json | | | |
| postgres-jsonb | | | |
| postgres-text | 232 | 253 | |

## Goals
* Use tornado to accept JSON and write to target storage
* ~~Use docker~~
* JSON to cassandra
* ~~JSON to kafka~~
* ~~JSON to postgresql~~
* ~~JSON to mongodb~~
* ~~JSON to couchdb~~
* JSON to elastic search
* ~~JSON to rabbitmq~~
* Visualization software of all of the above(if it exists)
* Make all at least concurrent.. but determine which can be async and not.. and why
* Simple benchmarks of sync(if created) and async of each


## Extra goals - depends on how long the above takes
* ~~Compare using tornado async libraries vers python3 concurrent~~





