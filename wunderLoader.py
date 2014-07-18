import json
import requests
import time
import datetime
import calendar
from pymongo import MongoClient
client = MongoClient('mongodb://temp:t3mp5@kahana.mongohq.com:10062/environs')
db = client.environs
collection = db.history


years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
months = [07]
days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
		"11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
		"21","22","23","24","25","26","27","28","29","30"]




for y in years:
	for m in months:
		for d in days:
			date =  str(y) + str(m) + str(d)
			url = "http://api.wunderground.com/api/9598cc9e2d252686/history_%s/q/CA/moraga.json" % (date)
			resp = requests.get(url=url)
			data = json.loads(resp.text)
			for obs in data["history"]["observations"]:
				data = {
		 			 "humid": obs["hum"],
		  			 "temp": obs["tempi"],
		  			 "timestamp": {
		  			 		"year":obs["utcdate"]["year"],
		  			 		"mon": obs["utcdate"]["mon"],
		  			 		"mday": obs["utcdate"]["mday"],
		  			 		"hour": obs["utcdate"]["hour"]
		  			 		},
		  			 "location": {
		    			"lat": 37.855451,
		    			"long": -122.125955
		  			 },
		 			 "wspd": obs["wspdi"]
				}
				#collection.insert(data)
				print data
