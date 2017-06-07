# -*- coding: utf-8 -*-

import math

class IMC(object):
	def __init__(self,nome,peso,altura):
		self.nome 	= nome
		self.peso 	= peso
		self.altura = altura

	def calcular(self):
		imc = 0.00
		imc = self.peso/math.pow(self.altura,2)
		print 'A pessoa %s possui IMC igual a: %s' % (self.nome,imc)
