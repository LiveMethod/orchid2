from flask import Flask
from flask import request

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

# search (s)
# String
# TODO: should accept && (and), || (or), - (not)
# returns array of txns matching

@app.route('/api')
def get():
	# return "Hello Orchid!"
	print("request arguments:")
	args = request.args
	print(args)

	# create an array to store result objects
	results = []

	if 's' in args:
		print("LOG: s in args")
		# Loop through every transaction
		for i, txn in enumerate(TRANSACTIONS):
			# For every piece of data in that transaction
			for key in txn:
				# convert the value to a string
				val = str(txn[key])
				# If the query is in that string
				if args['s'] in val:
					print("LOG: found a matching transaction")
					# Add the transaction to the results
					results.append(TRANSACTIONS[i])
					# Break to avoid double adding when
					# multiple values match the query
					break

	matches = str(results)

	return matches

if __name__ == '__main__':
	app.run()
