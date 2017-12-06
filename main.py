from helpers.instrument_helper import InstrumentHelper
import time
import sys

params = sys.argv


if(len(sys.argv[1:])):
	_instrument = str(params[1])
	_period = str(params[2])
else:
	_instrument = 'EUR_USD'
	_period = 60

instrument_helper = InstrumentHelper()
while True:
	print instrument_helper.get_info(_instrument)
	time.sleep(float(_period))