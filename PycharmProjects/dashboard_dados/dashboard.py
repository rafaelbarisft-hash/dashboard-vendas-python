import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# leitura dos dados CSV
df = pd.read_csv("PycharmProjects/dashboard_dados/vendas.csv")

# título
st.title("Dashboard de Vendas")

# mostrar tabela
st.subheader("Tabela de Vendas")
st.dataframe(df)

# métricas
faturamento = df['valor'].sum()
quantidade = df['quantidade'].sum()

st.metric("Faturamento Total", f"R$ {faturamento}")
st.metric("Quantidade Vendida", quantidade)

# gráfico de vendas por produto
st.subheader("Vendas por Produto")

grafico_produtos = df.groupby('produto')['valor'].sum()

fig, ax = plt.subplots()

ax.bar(grafico_produtos.index, grafico_produtos.values)

plt.xticks(rotation=45)

st.pyplot(fig)

# gráfico por categoria
st.subheader("Vendas por Categoria")

grafico_categoria = df.groupby('categoria')['valor'].sum()

fig2, ax2 = plt.subplots()

ax2.pie(
    grafico_categoria.values,
    labels=grafico_categoria.index,
    autopct='%1.1f%%'
)

st.pyplot(fig2)