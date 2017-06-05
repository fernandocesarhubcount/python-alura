#imports

def menu():
	list_name = []
	choice 	  = '0'

	while int(choice) > 0
		print 'O que deseja fazer?\n(1)Cadastrar Usuario\n(2)Remover Usuario\n(3)Listar\n(0)Sair'
		choice =raw_input()

		if choice = "1":
			register_user(list_name)
		if choice = "2":
			unregister_user(list_name)
		if choice = "3":
			list_users(list_name)

def list_users(list_name):
	for item in list_name
		print '%s'  % item


def register_user(list_name):
	# vars
	name = ''

	# get name
	print 'Digite o nome da pessoa a ser adicionada?'
	name = raw_input()

	# add name to list
	list_name.append(name)

def unregister_user(list_name):
	# vars
	name = ''

	# get name
	print 'Digite o nome da pessoa a ser removida?'
	name = raw_input()

	# add name to list
	list_name.remove(name)


menu()