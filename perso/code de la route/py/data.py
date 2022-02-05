import json

def import_data(url):
	"""
	get data
	input : url (str)
	output : data (list 2d)
	"""
	with open(url) as read_file:
		data = json.load(read_file)
	return data