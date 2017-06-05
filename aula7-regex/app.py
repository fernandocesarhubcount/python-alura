# -*- coding: utf-8 -*-

import re

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = '|'.join(nomes)
    resultado = re.match(regex,nomes_concatenados)
    print '%s' % (''.join(resultado.group()))

procurar_regex(['Fernando','Carol','Sheila','Paulo'])
