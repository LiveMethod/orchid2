# Normalizers are utils that convert various vendor-specific
# transaction data into uniform orchid-formatted transactions.

# For many interesting ideas, see: 
# https://developers.braintreepayments.com/reference/response/transaction/python

# Assigns data to the util for a given vendor
def normalize(vendor, data):
	# Assignment steps
	normalized_data = None

	if vendor == 'simple':
		normalized_data = vendor_simple(data)
	else:
		raise ValueError(vendor + ' is not a recognized vendor')
	#elsifs for other vendors here eventually

	# Verify that the normalized data is correct

	# This is the orchid schema. The readme is the source of truth
	# for the schema. If this file and the readme conflict, then
	# the readme wins.

	'''
	transaction: {
		UUID: string
		amount: number
		time: number // (unix time)
		type: string // (credit, debit, etc)
		state: string // (authorized, pending, settled, refunded, etc)
		description: string // typically the merchant name
		categories: [string, string, ...]// array of merchant0-side categories
		geodata: { // See note
			city: string,
			state: string, // 2 letter state, caps
			lat: number, // to 5 places, like 38.81602
			lon: number,
			timezone: string, // like "America/New_York"
		}
		custom:{
			necessity: number // 1 through 5
			categories: [{string,number}, ...] // see note
			notes: string // sanitized
		}
	}
	'''
	
	# Make sure the value was actually set
	if normalized_data is not None:
		
		# confirm that the object contains the expected things
		
		# note: this is untested, and might return something like
		# len(str(json)) which would be huge and wrong.
		data_length = str(len(normalized_data))
		if data_length != 9:
			raise ValueError('expected 9 objects in transaction. got ' + data_length)

		# UUID should be a string
		uuid_type = type(normalized_data.uuid)
		if uuid_type is not str:
			raise ValueError('uuid should be string but was ' + str(uuid_type))

		# amount should be a number
		amount_type = type(normalized_data.amount)
		if amount_type is not int:
			raise ValueError('uuid should be int but was ' + str(amount_type))

		# amount should be sane
		amount_length = len(normalized_data.amount)
		if amount_length <= 2 or amount_length >= 8
			raise ValueError('amount should be 3 to 8 digits long. was ' + amount_length)

		# todo: confirm that time is a real datetime type thing

		# todo: confirm that time is between sane intervals (eg 2010 and current day)

		# fixme: there needs to be a standard around how type/state/etc
		# are cased.

		# todo: export this to some kind of config file
		# this is fake for now until we see what kinds of things come in.
		valid_types = [
			"credit",
			"debit"
		]

		# confirm that the type is one that's recognized
		if normalized_data.type not in valid_types:
			raise ValueError('invalid transaction type: ' + normalized_data.type)

		# todo: export this to some kind of config file
		# this is fake for now until we see what kinds of things come in.
		valid_states = [
			"HOLD",
			"AUTHORIZED",
			"SETTLED",
			"DECLINED",
			"REVERSED"
		]

		# confirm that the state is one that's recognized
		if normalized_data.state not in valid_states:
			raise ValueError('invalid transaction state: ' + normalized_data.state)

		# description should be a string
		desc_type = type(normalized_data.description)
		if desc_type is not str:
			raise ValueError('description should be string but was ' + str(desc_type))

		# vendor categories should be a list
		vendor_cat_type = type(normalized_data.categories)
		if vendor_cat_type is not list:
			raise ValueError('categories should be list. was ' + str(vendor_cat_type))

		# vendor category list length should be sane
		if len(normalized_data.categories) > 20:
			raise ValueError('Maximum 20 vendor categories')

		for entry in normalized_data.categories:
			entry_type = type(entry)
			# every entry in the vendor categories should be a string
			if entry_type is not str:
				raise ValueError('All vendor categories should be strings. was ' + entry)
			# name length should be sane
			if len(entry) > 99:
				raise ValueError('Vendor category max length is 100. ' + entry)

		# TODO: geofilter and down

# Processing specific to bank simple
def vendor_simple(data):
	# This is the simple schema as of ~2016. This API is volatile
	# and subject to frequent change. If responses no longer match,
	# it's likely the response changed and the normalizer needs to
	# be updated.

	'''
	"transactions":[
		{
			"uuid":"58c2c7b2-101b-3a2d-a32d-2ea002a15491",
			"user_id":"b5fc2633-0440-4dea-83a0-ce3c6ecaaa10",
			"amounts":{
				"amount":129500,
				"cleared":129500,
				"fees":0,
				"cashback":0,
				"base":129500
				},
			"times":{
				"when_recorded":1451928756000,
				"when_recorded_local":"2016-01-04 12:32:36.0",
				"when_received":1451928757014,
				"last_modified":1451928757014,
				"last_txvia":1451928757014
				},
			"is_active":true,
			"record_type":"HOLD",
			"transaction_type":"signature_purchase",
			"bookkeeping_type":"debit",
			"is_hold":true,
			"running_balance":110432700,
			"raw_description":"CHICK-FIL-A #01831",
			"goal_id":null,
			"description":"Chick Fil A",
			"categories":[
				{
					"uuid":"208",
					"name":"Fast Food",
					"folder":"Food & Drink"
				}],
			"geo":{
				"city":"Fairfax",
				"state":"VA",
				"lat":38.81602,
				"lon":-77.25625,
				"timezone":"America/New_York"
				},
			"memo":null,
			"labels":null,
			"frequency":null,
			"arroway_id":null
		},
		...
	]
	'''

	vendor_categories = data.categories
	orchid_categories = []
	for entry in vendor_categories:
		orchid_categories.append(entry.name)

	notes_if_present = None
	if data.memo:
		notes_if_present = data.memo

	transaction = {
		'UUID': data.uuid,
		# I have no knowledge that this is the best of the amounts to use.
		# It's rare to have an event where all amounts are not equal.
		# I've never encountered one personally.
		'amount': data.amounts.amount,
		'time': 'TODO', # convert data.times.when_recorded from MS to saner time.
		'type': data.bookkeeping_type,
		'state': data.record_type, # This is in the format "HOLD". May need conversion.
		"raw_description": data.raw_description,
		'description': data.description, # typically the merchant name
		'categories': orchid_categories, # array of merchant-side category names
		'geodata': data.geo, # schema is based on simple's geo info
		'custom':{
			'necessity': None, # TODO: guess this? eg rules like "fast food MCC always 1"
			'categories': None, # TODO: pick orchid categories based on vendor's?
			'notes': notes_if_present # sanitized
		}
	}



# Add the normalized transactions to the database
def upsert(data):
	# upsert the data into mongodb