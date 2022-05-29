from flask import Flask
from gevent.pywsgi import WSGIServer
import yaml
import requests
from datetime import datetime
import socket

class LocationException(Exception):
  def __init__(self, message):
    self.message = message

def at_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

app=Flask(__name__)

def read_config(file_name):
    with open(file_name, 'r') as file:
        load_config = yaml.safe_load(file)
        url=load_config['url']
        loc=load_config["location"]
    return url,loc

def check_rainfall(url,loc):
    resp=requests.get(url)
    status=""
    if resp.status_code == 200:
        timestamp=resp.json()["items"][0]["timestamp"]
        time=timestamp.split('T')[1][0:5]
        station_readings=resp.json()["items"][0]["readings"]
        reading_unit=resp.json()["metadata"]["reading_unit"]
        for station in resp.json()["metadata"]["stations"]:
            if station['name'] == loc:
                for reading in station_readings:
                    if reading["station_id"]==station['id']:
                        status="Raining" if reading["value"] >0 else "Not Raining"
                        output=station['name']+', '+time+', '+str(reading["value"])+reading_unit+', '+status
                        break
                status="found"
                break
        if status=="":
           raise LocationException("Location "+loc+" doesn't exist")
    else:
        print(at_time()+" - URL=> "+url+" is not correct")
        output="There is some internal error. Please contact the admin"
    return output

@app.route('/')
def query_rainfall():
    try:
        url,loc=read_config("conf/config.yaml")
        return check_rainfall(url,loc)
    except Exception as e:
        print(at_time()+" - "+str(e))
        return "There is some internal error. Please contact the admin"

if __name__=='__main__':
    http_server = WSGIServer(('',8080),app)
    print(at_time()+" - Rainfall Service started on "+ socket.gethostbyname(socket.gethostname())+':8080')
    http_server.serve_forever()
