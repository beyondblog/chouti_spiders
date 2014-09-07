#/use/bin/evn python

from datetime import datetime
from elasticsearch import Elasticsearch
import json


class ChoutiElasticsearch(object):

    def __init__(self):
       self.es = Elasticsearch()

    def create_index(self,title,url):
        self.es.index(index="chouti", doc_type="chouti-type", body = { "title": title,"url": url, "timestamp": datetime.now() });


if __name__ == '__main__':
    search = ChoutiElasticsearch()


    jsonFile = open('chouti.json',"r")

    for line in jsonFile:
        obj = json.loads(line);
        title = obj['title']
        url = obj['url']
        search.create_index(title,url)

    jsonFile.close()
    print "create index success!"




