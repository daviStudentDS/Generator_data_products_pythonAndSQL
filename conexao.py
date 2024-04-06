import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='dados_produtos',
        user='sqluser',
        password='password'
    )
    if conn.is_connected():
        print('Conexão estabelecida com sucesso.')
except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")