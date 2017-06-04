#imports

from datetime import date

def calc_age():
	# vars
	todays_year = date.today().year
	year 		= int(raw_input())

	# get years
	print 'Qual o ano que voce nasceu?'
	 
	#calc and print
	print 'Voce tem %s ano(s)' % (todays_year - year)

def register_user(list_name):
	# vars
	name = ''

	# get name
	print 'Digite o nome da pessoa a ser adicionada?'
	name = raw_input()

	# add name to list
	list_name.append(name)

	return list_name

def unregister_user(list_name):
	# vars
	name = ''

	# get name
	print 'Digite o nome da pessoa a ser removida?'
	name = raw_input()

	# add name to list
	list_name.remove(name)

	return list_name
