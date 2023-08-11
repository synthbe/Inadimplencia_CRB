import pandas as pd

from save import planilha_geral as pg, planilha_atrasados as pa
from busca_binaria import busca_binaria
from regex import regex 

# Array dos codigos dos clientes da planilha geral para encontrar o numero dos atrasados
codigos_gerais = pg["Código"] 

#Dataframe que gerará um nova planilha filtrada
colunas = ['Nome', 'CPF', 'Telefone', 'Parcelas', 'Endereco', 'Cep', 'Cidade']
new_df = pd.DataFrame(columns=colunas)

passador = 0

for i, k in enumerate(pa["Código"]):
    ind = busca_binaria(k, codigos_gerais, 0, len(codigos_gerais) - 1) #Encontrar index do cliente atrasado na planilha geral
    if ind == -1: #Caso não ache na planilha, prossiga
        continue
    
    tel = pg.loc[ind, "Telefone"]
    if pd.isna(tel):
        continue
    else:
        tel = regex(tel) #Aplica um regex no telefone

    #Atribuição das variáveis para preencher a planilha filtrada
    nome = pg.loc[ind, "Nome"]
    cpf = pg.loc[ind, "CPF/CNPJ"]
    parc = str(pa.loc[i, "Parcelas"]) + "+"
    ender = pg.loc[ind, "Endereço"]
    cep = pg.loc[ind, "CEP"]
    cid = pg.loc[ind, "Cidade/UF"]    

    new_df.loc[passador, "Nome"] = nome
    new_df.loc[passador, "CPF"] = cpf
    new_df.loc[passador, "Telefone"] = tel
    new_df.loc[passador, "Parcelas"] = parc
    new_df.loc[passador, "Endereco"] = ender
    new_df.loc[passador, "Cep"] = cep
    new_df.loc[passador, "Cidade"] = cid

    passador += 1
    
filtrada = pd.DataFrame(new_df)
filtrada.to_excel("../planilhas/filtrados.xlsx", index=False)