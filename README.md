# rainfall-service [Get rainfall readings across Singapore]

It is a simple web application that extracts rainfall data of a particular location across Singapore, such as Gardens by the Bay (with address Marina Gardens Drive). The real-time weather readings can be found at https://api.data.gov.sg/v1/environment/rainfall. 
pip install -r requirements.txt
The application is developed as a webservice to serve the selected rainfall data over HTTP using Flask, a micro web framework written in Python.

It uses a config file(**config.yaml**) with the below 2 entries

    1. url: https://api.data.gov.sg/v1/environment/rainfall
    2. location: Marina Gardens Drive
**Output**

Location, Time, Rainfall Amount, Raining/Not Raining

**Example:**

When your app is running, calling http://localhost:8080 will return the current data for the given location, as a single line:
Marina Gardens Drive, 08:45, 0.2mm, Raining
