import json
import requests
import time
import datetime
from pymongo import MongoClient
client = MongoClient('mongodb://temp:t3mp5@kahana.mongohq.com:10062/environs')
db = client.environs
collection = db.environs

url = 'https://api.spark.io/v1/devices/55ff69065075555332311787/temperature?access_token=2455a5328b9c73b737fdee162117fc6ca71d323e'

while True:
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	temp = (9/5) * ( ( (((data["result"] - .5) * 3.3)/4095)) * 100 ) + 32
	data = {
 			 "humid": 0,
  			 "temp": ("%.2f" % temp),
  			 "timestamp": datetime.datetime.utcnow(),
  			 "devID": "55ff69065075555332311787",
  			 "location": {
    			"lat": 37.855451,
    			"long": -122.125955
  			 },
 			 "wspd": 0
			}
	temp_id = collection.insert(data)
	print temp_id
	time.sleep(60)
