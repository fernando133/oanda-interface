from helpers.instrument_helper import InstrumentHelper
import time
import sys
import pymongo
from pymongo import MongoClient

params = sys.argv

client = MongoClient()
client = MongoClient('mongodb://tcc2:root@ds211029.mlab.com:11029/historical_eur_usd')
db = client['historical_eur_usd']
collection = db['eur_usd']

if(len(sys.argv[1:])):
	_instrument = str(params[1])
	_period = str(params[2])
else:
	_instrument = 'EUR_USD'
	_period = 60

instrument_helper = InstrumentHelper()
while True:
	data = instrument_helper.get_info(_instrument)
	print data
	data_id = collection.insert_one(data).inserted_id
	print data_id
	time.sleep(float(_period))