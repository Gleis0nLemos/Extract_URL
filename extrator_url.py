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


url = "https://bytebank.com/cambio?quantidade=100&&moedaOrigem=real&moedaDestino=dolar"
#extrator_url = ExtratorURL(None)
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print(valor_quantidade)



