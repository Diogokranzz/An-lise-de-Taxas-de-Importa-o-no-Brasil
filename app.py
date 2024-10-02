import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# Criar um DataFrame fictício de taxas de importação em cidades do Brasil
data = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Taxa de Importação (%)': [15, 20, 18, 10, 22, 17],
    'Valor Importado (R$)': [5000000, 3000000, 2000000, 1500000, 2500000, 1000000]
}
df = pd.DataFrame(data)

# Título do aplicativo
st.title("Análise de Taxas de Importação no Brasil")

# Exibir o DataFrame
st.subheader("Dados de Taxas de Importação")
st.dataframe(df)

# Gráfico de barras interativo da taxa de importação por cidade
st.subheader("Taxa de Importação por Cidade")
fig_bar = px.bar(df, 
                  x='Cidade', 
                  y='Taxa de Importação (%)', 
                  title='Taxa de Importação por Cidade no Brasil',
                  text='Taxa de Importação (%)',
                  color='Taxa de Importação (%)',
                  color_continuous_scale=px.colors.sequential.Viridis)

fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
st.plotly_chart(fig_bar)

# Gráfico de dispersão interativo
st.subheader("Relação entre Valor Importado e Taxa de Importação")
fig_scatter = px.scatter(df, 
                         x='Valor Importado (R$)', 
                         y='Taxa de Importação (%)', 
                         color='Cidade', 
                         size='Valor Importado (R$)', 
                         hover_name='Cidade',
                         title='Relação entre Valor Importado e Taxa de Importação',
                         size_max=60)

st.plotly_chart(fig_scatter)

# Modelo de regressão linear simples
st.subheader("Previsão de Taxa de Importação")
X = df[['Valor Importado (R$)']]
y = df['Taxa de Importação (%)']

# Criar e treinar o modelo
model = LinearRegression()
model.fit(X, y)

# Entrada do usuário
valor_importado_input = st.number_input("Valor Importado (R$)", min_value=0, max_value=10000000, step=1000)
predicted_tax = model.predict(np.array([[valor_importado_input]]))

# Mostrar resultado da previsão
if st.button('Prever Taxa de Importação'):
    st.write(f"A taxa de importação prevista para um valor de {valor_importado_input} R$ é: {predicted_tax[0]:.2f}%")