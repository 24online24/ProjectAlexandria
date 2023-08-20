import os
import json
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])


def get_jsons():
    path = os.path.dirname(os.getcwd())
    target_path = os.path.join(path, 'ArchivedPosts\\techsupport')

    for file in os.listdir(target_path):
        f = open(os.path.join(target_path, file))
        yield json.load(f)


if __name__ == '__main__':
    for document in get_jsons():
        print(document['id'], document['author'])
        res = es.index(index='reddit-techsupport', id=document['id'], document=document)
        print(res['result'])
