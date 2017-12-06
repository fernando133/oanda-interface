import oandapy
from conf.config import Config

class InstrumentHelper:
	def __init__(cls):
		cfg = Config()
		cls.account_id = cfg.get_oanda_env('account_id')
		cls.api_key = cfg.get_oanda_env('api_key')
		cls.oanda = oandapy.API(environment='practice', access_token=cls.api_key)

	def get_info(cls, instrument):
		"""
		Get real time info for a specific instrument.
		E.g: 'EUR_USD', 'USD_JPY'
		"""
		response = cls.oanda.get_prices(instruments=instrument)
		return response

