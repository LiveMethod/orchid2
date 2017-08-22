from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from urllib.parse import urlparse, parse_qsl
from src.filters import filters
from src.normalizers import normalizers
import json

app = Flask(__name__)

# Declare DB name for pymongo to connect to
app.config['MONGO_DBNAME'] = 'temp'
mongo = PyMongo(app)

@app.route('/api')
def get():
	# without encoding, this would be returned as bytestring
	query_raw = str(request.query_string,'utf-8')

	# parse_qsl() on a raw query string is superior to
	# request.args here because it ensures that the
	# returned items are in the correct order. 
	# https://docs.python.org/2/library/urlparse.html
	query_list = parse_qsl(query_raw)
	
	# get all transactions from mongo
	raw_data = mongo.db.transactions.find();
	# convert mongo's bson to a python list
	data = json_util.loads(json_util.dumps(raw_data))
	
	# process commands from query
	for i, process in enumerate(query_list):
		query = query_list[i][0]
		value = query_list[i][1]
		# print('calling filter ' + query + ' for ' + value)

		data = filters.get_filter_for(query, value, data)
	return str(data)

# for a given collection name, destroy the collection and
# create a blank one of the same name
@app.route('/reset/collection/<name>')
def reset_collection(name):
	mongo.db.drop_collection(name)
	mongo.db.get_collection(name)
	message = "Welp, there you go. " + name + " is empty. You're welcome."
	return message

# import the demo data for a given vendor
@app.route('/import/vendor/<vendor>')
def import_transactions(vendor):
	txns = None
	if vendor == 'simple':
		# if this breaks in the future, it's been moved around a little.
		# troubleshoot folder nesting first.
		with open('../../secrets/demo_vendor_txns/simple_transactions.json') as data:
			txns = json.load(data)
			txns = txns['transactions']

		for txn in txns:
			clean_data = normalizers.normalize('simple', txn)
			mongo.db.transactions.update_one({'uuid' : clean_data['uuid']}, {"$set": clean_data}, upsert = True)

		message = "Inserted " + str(len(txns)) + " transactions."
		return message
	else:
		message = str(vendor) + " is not a recognized vendor."
		return message

if __name__ == '__main__':
	app.run()
