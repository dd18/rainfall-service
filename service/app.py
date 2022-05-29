from flask import Flask
from gevent.pywsgi import WSGIServer
import yaml

app=Flask(__name__)
@app.route('/')
def query_rainfall():
    return "Raining"

def read_config(file_name):
    with open(file_name, 'r') as file:
        load_config = yaml.safe_load(file)
        url=load_config['url']
        loc=load_config["location"]
    return url,loc

if __name__=='__main__':
    http_server = WSGIServer(('',8080),app)
    http_server.serve_forever()
