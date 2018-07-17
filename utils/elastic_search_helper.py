# coding: utf-8


from elasticsearch import Elasticsearch

_index = 'school'
_type = 'name'
es_url = 'http://localhost:9200/'
es = Elasticsearch(es_url)


def bulk_es(chunk_data):
    response = es.index(_index, _type, chunk_data)
    print(response['result'])
    print(response['_shards'])


with open('school.json', encoding='utf-8') as f:
    schools = eval(f.read())
    for index, school in enumerate(schools):
        print('index=%s' % str(index))
        bulk_es(school)
