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

def give_data(url,data):
	"""
	remplace un fichier json par une nouvelle valeur
	"""
	with open(url,"w") as fp:
		json.dump(data,fp)
