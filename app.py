from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qsl
from src.filters import filters
app = Flask(__name__)

# Mock data
TRANSACTIONS = [
	{
		'id': '01',
		'merchant': 'tom',
		'amount': '10000',
		'date': '1502781222'
	},
	{
		'id': '02',
		'merchant': 'd1ck',
		'amount': '50000',
		'date': '1502582400'
	},
	{
		'id': '03',
		'merchant': 'harry',
		'amount': '999999',
		'date': '1480941859'
	}
]

@app.route('/api')
def get():
	# request.args will return all arguments
	# broken out into a dict, but it doesn't
	# assure that the order of the args matches
	# their original order in the URL. This is bad.

	# Instead, we feed the raw query string into
	# parse_qsl(), which returns a similar set of
	# key value pairs, but in the form of a list
	# which guarantees the correct order. 
	# https://docs.python.org/2/library/urlparse.html

	# without encoding, this will be returned as bytestring
	query_raw = str(request.query_string,'utf-8')
	query_list = parse_qsl(query_raw)
	
	# results start off with everything in scope
	data = TRANSACTIONS;

	for i, process in enumerate(query_list):
		query = query_list[i][0]
		value = query_list[i][1]
		print('calling ' + query + ' for ' + value)

		data = filters.get_filter_for(query, value, data)
	return str(data)

if __name__ == '__main__':
	app.run()
