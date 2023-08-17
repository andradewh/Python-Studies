'''
Informações a cálcular / Ações a tomar:

0.0 - Importar base de dados
0.1 - Visualizar base de dados
1 - Faturamento por loja
2 - Quantidade de produtos vendidos por loja
3 - Ticket médio por loja

'''
import pandas as pd

#0.0
df = pd.read_excel('Arquivos_Estudos/minicurso_python_hashtag/Vendas.xlsx')

#0.1
pd.set_option('display.max_columns', None)
#print(df.head())

#1
df_fat_loja = df[['ID Loja','Valor Final']].groupby('ID Loja').sum()
#print(df_fat_loja.head())

#2
df_qtd_produtos_loja = df[['ID Loja','Quantidade']].groupby('ID Loja').sum()
#print(df_qtd_produtos_loja.head())

#3
df_ticket_medio = (df_fat_loja['Valor Final'] / df_qtd_produtos_loja['Quantidade']).to_frame()
#print(df_ticket_medio.head())