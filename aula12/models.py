# -*- coding: utf-8 -*-

import file

class Perfil(object):
	def __init__(self,nome,telefone,empresa):
		self.nome 	  	= nome
		self.telefone 	= telefone
		self.empresa  	= empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'O cadastro do(a) %s de telefone %s pertence a empresa %s e possui %s curtida(s)' % (self.nome, self.telefone, self.empresa, self.pegar_curtidas())

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	@staticmethod
	def exportar_perfil(self):
		file = File('download/profiles.csv')
		file.write(*profile)

	@classmethod
	def importar_perfis():	

class Perfil_Vip(Perfil):
	def __init__(self, nome,telefone,empresa,apelido):
		super(Perfil_Vip, self).__init__(nome,telefone,empresa,apelido='')
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas()*10.0

