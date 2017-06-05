# -*- coding: UTF-8 -*-

def menu():
	list_name = []
	choice 	  = ''

	while choice != '0' :
		print 'O que deseja fazer?\n(1)Cadastrar Usuario\n(2)Remover Usuario\n(3)Listar\n(4)Alterar Usuario\n(0)Sair'
		choice =raw_input()

		if choice == "1":
			register_user(list_name)
		if choice == "2":
			unregister_user(list_name)
		if choice == "3":
			list_users(list_name)
		if choice == "4":
			change_user(list_name)

def list_users(list_name):
	for item in list_name:
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

def change_user(list_name):
	# vars
	name 	   = ''
	name_index = 0

	# get name
	print 'Digite o nome da pessoa a ser alterada?'
	name = raw_input()

	if name in list_name:
		name_index = list_name.index(name)
		print 'Altere o nome (%s)' % (name)
		name 				  = raw_input()		
		list_name[name_index] = name
	else:
		print 'Nao e possivel alterar esse nome, ele nao esta cadastrado'


menu()