import os
from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from urllib.parse import urlparse, parse_qsl
from src.filters import filters

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'temp'
mongo = PyMongo(app)

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

	# without encoding, this would be returned as bytestring
	query_raw = str(request.query_string,'utf-8')
	query_list = parse_qsl(query_raw)
	
	# get all transactions from mongo
	raw_data = mongo.db.transactions.find();
	# convert mongo's bson to a python list
	data = json_util.loads(json_util.dumps(raw_data))
	
	# process commands from query
	for i, process in enumerate(query_list):
		query = query_list[i][0]
		value = query_list[i][1]
		print('calling ' + query + ' for ' + value)

		data = filters.get_filter_for(query, value, data)
	return str(data)

if __name__ == '__main__':
	app.run()
