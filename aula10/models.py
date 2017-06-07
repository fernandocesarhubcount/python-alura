# -*- coding: utf-8 -*-

class Perfil(object):
	def __init__(self,nome,telefone,empresa):
		self.nome 	  	= nome
		self.telefone 	= telefone
		self.empresa  	= empresa
		# self.curtidas 	= 0
		self.__curtidas = 0

	def imprimir(self):
		# print 'O cadastro do(a) %s de telefone %s pertence a empresa %s e possui %s curtida(s)' % (self.nome, self.telefone, self.empresa, self.curtidas)
		print 'O cadastro do(a) %s de telefone %s pertence a empresa %s e possui %s curtida(s)' % (self.nome, self.telefone, self.empresa, self.pegar_curtidas())

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

class Perfil_Vip(Perfil):
	def __init__(self, nome,telefone,empresa,apelido):
		super(Perfil_Vip, self).__init__(nome,telefone,empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas()*10.0


