from pymongo import MongoClient
from datetime import datetime


def loadData(filename):
	URI = "mongodb://accountAdmin01:changeMe@127.0.0.1:27017/test"
	client = MongoClient(URI)
	db = client.test
	db = client.test.dini
	f = open(filename,'r').read().strip().split("\n")
	for line in f:
		record = line.split(",")
		record = [ int(e) for e in record]
		print record
		data = {"ph_no": record[0],"date ":str(datetime.now()) , "temp" :record[1]}
		db.insert_one(data)

loadData("rawdata.txt")