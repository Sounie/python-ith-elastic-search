from elasticsearch7 import Elasticsearch

def do_stuff():
    client = Elasticsearch("http://localhost:9200")
    infoResp = client.info()

    print(f'Cluster info: {infoResp}')

if __name__ == '__main__':
    do_stuff()
