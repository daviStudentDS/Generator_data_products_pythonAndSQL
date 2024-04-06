import mysql.connector
import pandas as pd

# Configuração da conexão
config = {
 'user': 'sqluser',
 'password': 'password',
 'host': 'localhost',
 'database': 'dados_produtos',
 'raise_on_warnings': True
}

# Conectando ao banco de dados
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Lendo o arquivo CSV
df = pd.read_csv('vendas_produtos.csv')

# Inserindo os dados na tabela
for index, row in df.iterrows():
    sql = """INSERT INTO vendas_produtos (ID_Produto, Quantidade, Preco_Unitario, Data_Venda)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, tuple(row))

# Confirmando as alterações
cnx.commit()

# Fechando a conexão
cursor.close()
cnx.close()
