# rainfall-service [Get rainfall readings across Singapore]
## Overview

It is a simple web application that extracts rainfall data of a particular location across Singapore, such as Gardens by the Bay (with address Marina Gardens Drive). The real-time weather readings can be found at https://api.data.gov.sg/v1/environment/rainfall. 

The application is developed as a webservice to serve the selected rainfall data over HTTP using Flask, a micro web framework written in Python.

It uses a config file(**config.yaml**) with the below 2 entries

    url: https://api.data.gov.sg/v1/environment/rainfall
    location: Marina Gardens Drive

**Output**

Location, Time, Rainfall Amount, Raining/Not Raining

**Example:**

When your app is running, calling http://localhost:8080 will return the current data for the given location, as a single line:

Marina Gardens Drive, 08:45, 0.2mm, Raining

## Installation, Setup and Run
#### On Physical machine/ VM

Clone the repo

    git clone https://github.com/dd18/rainfall-service.git 
   
Install the python dependencies

    cd rainfall-service/
    pip install -r requirements.txt
   
Run the application

    python service/app.py
      
Test

    curl -X GET http://localhost:8080

#### On Docker

Clone the repo

    git clone https://github.com/dd18/rainfall-service.git
        
Create the docker image
        
    cd rainfall-service/
    docker build -t rainfallsvc .

Check the docker images
    
    docker images

Run the app in the container

    docker run -d -p 8080:8080 -v $(pwd)/conf/config.yaml:/app/conf/config.yaml --name rainfall rainfallsvc
    
Test

    curl -X GET http://localhost:8080

#### On Kubernetes

rainfall docker image is pushed to [dockerhub](https://hub.docker.com/repository/docker/docklinux/rainfall) and is publicly available with the tag **docklinux/rainfall**. POD definition file pulls the docker image from [dockerhub](https://hub.docker.com/repository/docker/docklinux/rainfall).

To pull the docker image

    docker pull docklinux/rainfall

Create the namespace

    kubectl create ns rainfall

Create the configmap

*using config.yaml*

    git clone https://github.com/dd18/rainfall-service.git
    cd rainfall-service/
    kubectl create configmap rainfall-config --from-file conf/config.yaml -n rainfall
                               
*Or using manifest*
                             
    git clone https://github.com/dd18/rainfall-service.git
    cd rainfall-service/
    kubectl apply -f manifests/rainfall-cm.yaml

Create the Pod

    kubectl apply -f manifests/rainfall-pod.yaml
    
Port Forwarding
 
    kubectl port-forward rainfall -n rainfall 8080:8080

Test

    curl -X GET http://localhost:8080
    
    
        
