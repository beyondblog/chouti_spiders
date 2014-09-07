#coding=utf

from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()

#print(es.get(index="user", doc_type="test-type", id=1)['_source'])

es.indices.refresh(index="chouti");


#res = es.search(index="user", body={"query": {"match_all": {}}})

res = es.search(index="chouti",size = 10, body= {
                                    "query": {
                                       "match":{'title': '感觉'}
                                       #"wildcards":{"name":"github*"}
                                     },
                                    "sort":[{'timestamp': 'asc'}]
                                    });

print("search %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print("%(title)s" % hit['_source'])

pass

