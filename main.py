from elasticsearch7 import Elasticsearch

def print_hi(name):
    client = Elasticsearch("http://localhost:9200")
    resp = client.info()

    print(f'Cluster info: {resp}')


if __name__ == '__main__':
    print_hi('PyCharm')
