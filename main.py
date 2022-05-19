#traçado uma url de exemplo para consulta e extração de dados
url = "https://bytebank.com/cambio?quantidade=100&&moedaOrigem=real&moedaDestino=dolar"

#base, parametros
#find é usado para buscar alguma informação na string                            #procurando um caractere com .find
indice_interrogacao = url.find("?")                                              #search = "z" in url
url_base = url[:indice_interrogacao]                                             #print(search)
#a url base vai até o ponto de interrogação, é start da pesquisa basicamente
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)
#url parametros vem logo após o "?"


#Busca
parametros_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametros_busca)
#utilizando o método len para chegar ao final de um parametro assim passado
indice_valor = indice_parametro + len(parametros_busca) + 1
indice_ecomercial = url_parametros.find("&", indice_valor)
if indice_ecomercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_ecomercial]
print(valor)