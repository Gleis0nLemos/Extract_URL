import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL is empty")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametros(self, parametros_busca):
        indice_parametro = self.get_url_parametros().find(parametros_busca)
        indice_valor = indice_parametro + len(parametros_busca) + 1
        indice_ecomercial = self.get_url_parametros().find("&", indice_valor)
        if indice_ecomercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_ecomercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "URL base: " + self.get_url_base() + "\n" + "URL parametros: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url



# url = "https://bytebank.com/cambio?quantidade=100&&moedaOrigem=real&moedaDestino=dolar"
# #extrator_url = ExtratorURL(None)
# extrator_url = ExtratorURL(url)
# extrator_url_2 = ExtratorURL(url)
#
# parametro_busca = "moedaOrigem"
# valor_quantidade = extrator_url.get_valor_parametros(parametro_busca)
# print("{}:".format(parametro_busca), valor_quantidade)
# #poderia ser tambem(usando formatação de exibição):
# # param_tradução = {"moedaOrigem": "Moeda Origem","moedaDestino": "Moeda Destino","quantidade": "Quantidade"}
# # print(param_tradução[parametro_busca],": {}".format(valor_quantidade))
#
# print(extrator_url)
# print("O tamanho da URL é:", len(extrator_url), "caracteres!")
#
# print("Verificação de igualdade de objetos:", extrator_url == extrator_url_2)#mesmo que: extrator_url.__eq__extrator_url_2
# #objetos podem ser iguais, mais não são idênticos pois tem endereços de memória diferentes.
# #método eq sobrescreve essa verificação de endereço
# #o "is" verifica se realmente são idênticos
# print("id:", id(extrator_url))
# print("id:", id(extrator_url_2))


### CLASS CHALLENGE ###
#Conversão de Câmbio entre real/dolar
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametros("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametros("moedaDestino")
quantidade = extrator_url.get_valor_parametros("quantidade")

if moeda_destino == "real" and moeda_origem == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + f" reais equivale a ${valor_conversao:,.2f} dólares.")
elif moeda_destino == "dolar" and moeda_origem == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + f" dólares equivale a R${valor_conversao:,.2f} reais.")
else:
    print(f"O câmbio de conversão de {moeda_origem} para {moeda_destino} não tem disponibilidade")
