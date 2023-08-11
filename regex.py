import re

#Feito no bing

def regex(telefone):
    # Cria um padrão regex que corresponde a qualquer coisa que não seja um dígito
    padrao = re.compile("\D")
    # Substitui o padrão por uma string vazia na string telefone
    telefone_limpo = padrao.sub("", telefone)
    if len(telefone_limpo) < 11:
      # Adiciona o número "9" entre o segundo e o terceiro dígito
      telefone_limpo = telefone_limpo[:2] + "9" + telefone_limpo[2:]
    # Retorna o telefone limpo
    return telefone_limpo