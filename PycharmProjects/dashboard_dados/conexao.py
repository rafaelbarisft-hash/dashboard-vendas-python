import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dashboard_vendas'
)

print("Conectado com sucesso!")

query = "SELECT * FROM vendas"

df = pd.read_sql(query, conexao)

print(df)

# FATURAMENTO TOTAL
faturamento = df['valor'].sum()

print("\nFaturamento Total:")
print(f"R$ {faturamento}")

# QUANTIDADE TOTAL DE PRODUTOS
quantidade = df['quantidade'].sum()

print("\nQuantidade Vendida:")
print(quantidade)

# PRODUTO MAIS CARO
mais_caro = df.loc[df['valor'].idxmax()]

print("\nProduto Mais Caro:")
print(mais_caro['produto'])

conexao.close()