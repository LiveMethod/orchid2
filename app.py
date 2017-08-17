from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qsl

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
		'merchant': 'dick',
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

# Takes a filter abbreviation as a string
# returns the filter function for that abbreviation
def getFilterFor(filter, value, data):
	
	if filter == 's':
		return searchFilter(value, data)
	# If there's nothing to match the filter,
	# give the data back unmodified
	else:
		return data

# search (s)
# String
# TODO: should accept && (and), || (or), - (not)
def searchFilter(value, data):
	print('searchFilter: ' + value)
	matches = []

	# Loop through every transaction
	for i, txn in enumerate(data):
		# For every piece of data in that transaction
		for key in txn:
			# convert the value to a string
			val = str(txn[key])
			# If the query is in that string
			if value in val:
				# Add the transaction to the results
				matches.append(data[i])
				# Break to avoid double adding when
				# multiple values match the query
				break

	return matches

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

		data = getFilterFor(query, value, data)
	return str(data)

if __name__ == '__main__':
	app.run()
