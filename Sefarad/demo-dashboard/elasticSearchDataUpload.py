import elasticsearch
from elasticsearch_dsl import Search
import json
import requests

from elasticsearch import Elasticsearch

def upload():
    es = Elasticsearch(hosts='http://localhost:9200')
    with open('data3.json','r') as file:
        for line in file:
            doc=json.loads(line)
            res = es.index(index="tweetnutweetion8", doc_type='tweet',body=doc)
            if (res['result']!='created'):
                print(res['result'])
upload()
