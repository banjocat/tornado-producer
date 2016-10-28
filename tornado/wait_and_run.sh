./wait-for-it.sh kafka:9092
./wait-for-it.sh mongo:27017
./wait-for-it.sh elastic:9200
./wait-for-it.sh cassandra:9042
pypy3 server.py
