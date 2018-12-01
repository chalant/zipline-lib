from contrib.data.download.executors import alpha_vantage, wikipedia
from contrib.data.download.executors import tiingo
from contrib.data.download.executors import yahoo
from contrib.data.download.executors import RequestsCounter

_YAHOO_COUNTER = RequestsCounter(100)
_WIKIPEDIA = None
_TIINGO_COUNTER = RequestsCounter(20000)
_ALPHA_VANTAGE_COUNTER = RequestsCounter(1)
_WIKI_COUNTER = RequestsCounter(1)


# TODO: retrieve api keys from environment... don't hardcode it here...
def order_executor(name, api_key=None, full_access=False):
	global _WIKIPEDIA
	if name is 'AlphaVantage':
		return alpha_vantage._AlphaVantage(
			'alpha vantage',
			_ALPHA_VANTAGE_COUNTER,
			"5B3LVTJKR827Y06N")

	elif name is 'Yahoo':
		return yahoo._Yahoo(
			'yahoo',
			_YAHOO_COUNTER)

	elif name is 'Wikipedia':
		# ONLY one instance of this...
		if not _WIKIPEDIA:
			return wikipedia.WikipediaExecutor(
				'wiki',
				_WIKI_COUNTER)
		else:
			return _WIKIPEDIA

	elif name is 'Tiingo':
		return tiingo._Tiingo(
			'tiingo',
			"595f4f7db226d74f0d20e6b80880b80e4ae67806",
			_TIINGO_COUNTER,
			paid_account=full_access)

	else:
		raise ValueError(
			'No executor named {}'.format(name))