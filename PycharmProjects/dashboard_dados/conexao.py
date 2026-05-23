import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Ler arquivo CSV
df = pd.read_csv("vendas.csv")

# Título
st.title("Dashboard de Vendas")

# Mostrar tabela
st.subheader("Tabela de Vendas")
st.dataframe(df)

# FATURAMENTO TOTAL
faturamento = df['valor'].sum()

# QUANTIDADE TOTAL
quantidade = df['quantidade'].sum()

# Métricas
st.metric("Faturamento Total", f"R$ {faturamento}")
st.metric("Quantidade Vendida", quantidade)

# Gráfico de barras
st.subheader("Vendas por Produto")

grafico_produtos = df.groupby('produto')['valor'].sum()

fig, ax = plt.subplots()

ax.bar(grafico_produtos.index, grafico_produtos.values)

plt.xticks(rotation=45)

st.pyplot(fig)

# Gráfico pizza
st.subheader("Vendas por Categoria")

grafico_categoria = df.groupby('categoria')['valor'].sum()

fig2, ax2 = plt.subplots()

ax2.pie(
    grafico_categoria.values,
    labels=grafico_categoria.index,
    autopct='%1.1f%%'
)

st.pyplot(fig2)