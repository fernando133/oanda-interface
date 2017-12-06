import os
import json

class Config:
	def __init__(cls):
		file = open(os.path.abspath('conf/script_conf.json'), 'r')
		cls.conf = json.loads(file.read())
		cls._conf_key = 'script-conf'

	def get_oanda_env(cls,key):
		temp = cls.conf[cls._conf_key]
		temp = temp['oanda'][key]
		return str(temp)