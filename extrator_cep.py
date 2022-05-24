#Regular Expression -- RegEx
import re

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

#caracteristicas, cep: 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}?[0-9]{3}")
busca = padrao.search(endereco)  #Match: encontra na string o padrão passado a partir de um endereço
if busca:
    cep = busca.group()
    print(cep)