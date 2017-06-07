# -*- coding: utf-8 -*-

class Perfil(object):
	def __init__(self,nome,telefone,empresa):
		self.nome 	  = nome
		self.telefone = telefone
		self.empresa  = empresa

	def imprimir(self):
		print 'O cadastro do(a) %s de telefone %s pertence a empresa %s' % (self.nome, self.telefone, self.empresa)
