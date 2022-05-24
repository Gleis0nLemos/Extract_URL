#Exemplos de URLs válidas:
#     bytebank.com/cambio
#     bytebank.com.br/cambio
#     www.bytebank.com/cambio
#     www.bytebank.com.br/cambio
#     http://www.bytebank.com/cambio
#     http://www.bytebank.com.br/cambio
#     https://www.bytebank.com/cambio
#     https://www.bytebank.com.br/cambio
#
#Exemplos de URLs inválidas:
#     https://bytebank/cambio
#     https://bytebank.naoexiste/cambio
#     ht://bytebank.naoexiste/cambio


#url mais completa, para exemplo de código:
#https://www.bytebank.com.br/cambio
import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)#O search() vai buscar dentro de uma string se aquele padrão foi encontrado.
                             #o match() verifica se o padrão bate exatamente com a string passada.
if not match:
    raise ValueError("A URL não é válida")