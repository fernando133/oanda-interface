from helpers.instrument_helper import InstrumentHelper
import time
import sys
import pymongo
from pymongo import MongoClient

params = sys.argv

client = MongoClient()
client = MongoClient('mongodb://tcc2:root@ds211029.mlab.com:11029/historical_eur_usd')
db = client['historical_eur_usd']
collection = db['eur_usd_2']

if(len(sys.argv[1:])):
	instrument = str(params[1])
	period = str(params[2])
else:
	instrument = 'EUR_USD'
	period = 60

instrument_helper = InstrumentHelper()
while True:
	data = instrument_helper.get_info(instrument)
	print data['prices'][0]
	if data['prices'][0]['status'] != 'halted':
		data_id = collection.insert_one(data['prices'][0]).inserted_id
		print data_id
	
	time.sleep(float(period))