import os
import json

import tornado.ioloop
import tornado.web
from elasticsearch import Elasticsearch

ELASTIC = os.getenv('elastic', 'elastic')
PORT = os.getenv('elastic_port', 9200)
URL = "{0}:{1}".format(ELASTIC, PORT)


class ElasticHandler(tornado.web.RequestHandler):
    elastic = Elasticsearch([URL])

    def post(self):
        msg = self.request.body.decode('utf-8')
        data = json.loads(msg)
        self.elastic.index(index='test', doc_type='json', body=data)
        self.write('{"result": "success"}')
