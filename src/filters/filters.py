# Takes a filter abbreviation as a string
# returns the filter function for that abbreviation
def get_filter_for(filter, value, data):
	if filter == 's':
		return search(value, data)
	elif filter == 'm':
		return search_merchant(value, data)
	elif filter == 'l':
		return search_location(value, data)
	elif filter == 'id':
		return search_id(value, data)
	elif filter == 'dr':
		return date_range(value, data)
	else:
		# If there's nothing to match the filter,
		# give the data back unmodified
		return data

##############
############## Single input filters
##############

# search (s)
# TODO: should accept && (and), || (or), - (not)
def search(value, data):
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

# merchant (m)
# TODO: should accept && (and), || (or), - (not)
def search_merchant(value, data):
	matches = []

	# Loop through every transaction
	for i, txn in enumerate(data):
		# convert the value to a string
		val = str(txn['merchant'])
		# If the query is in that string
		if value in val:
			# Add the transaction to the results
			matches.append(data[i])
			# Break to avoid double adding when
			# multiple values match the query
			break

	return matches

# id (id)
# TODO: should accept && (and), || (or), - (not)
def search_id(value, data):
	matches = []

	# Loop through every transaction
	for i, txn in enumerate(data):
		# convert the value to a string
		val = str(txn['id'])
		# If the query is in that string
		if value in val:
			# Add the transaction to the results
			matches.append(data[i])
			# Break to avoid double adding when
			# multiple values match the query
			break

	return matches

# location (l)
# TODO: should accept && (and), || (or), - (not)
def search_location(value, data):
	print('TODO: location filter')
	return data

##############
############## Ranged input filters
##############

# daterange (dr)
def date_range(value, data):
	clean_value = None
	# A correctly formatted value has two
	# unix timestamps larger than 900000000
	# separated by a hyphen

	if '-' in value:
		# split at the hyphen
		ranges = str(value).split('-')
		
		# confirm that there are two values
		if len(ranges) == 2:
			rangeStart = ranges[0]
			rangeEnd = ranges[1]

			# if the two values are digits, convert them to int
			if rangeStart.isdigit() and rangeEnd.isdigit():
				rangeStart = int(rangeStart)
				rangeEnd = int(rangeEnd)
			else:
				raise ValueError('times should be numbers between larger than 900000000')
			
			# If the start comes after the end, swap them
			if rangeStart > rangeEnd:
				rangeStart, rangeEnd = rangeEnd, rangeStart
			# return
			clean_value = (rangeStart, rangeEnd)
		else:
			raise ValueError('input exceeded the expected two hyphen separated values.')
	else:
		raise ValueError('expected two unix timestamps separated by hyphen')


	matches = []

	if clean_value is not None:
		# Loop through every transaction
		for i, txn in enumerate(data):
			# convert the value to a string
			val = int(txn['date'])
			# If the value is within range
			if val >= clean_value[0] and val <= clean_value[1]:
				# Add the transaction to the results
				matches.append(data[i])
				# Break to avoid double adding when
				# multiple values match the query
				# break

	return matches
