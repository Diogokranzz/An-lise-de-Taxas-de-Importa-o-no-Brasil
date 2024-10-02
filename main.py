import pandas as pd
import plotly.express as px

# Criar um DataFrame fictício de taxas de importação em cidades do Brasil
data = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Taxa de Importação (%)': [15, 20, 18, 10, 22, 17],
    'Valor Importado (R$)': [5000000, 3000000, 2000000, 1500000, 2500000, 1000000]
}
df = pd.DataFrame(data)

# Visualizar as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Gráfico de barras interativo da taxa de importação por cidade
fig_bar = px.bar(df, 
                  x='Cidade', 
                  y='Taxa de Importação (%)', 
                  title='Taxa de Importação por Cidade no Brasil',
                  text='Taxa de Importação (%)',
                  color='Taxa de Importação (%)',
                  color_continuous_scale=px.colors.sequential.Viridis)

fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
fig_bar.update_layout(xaxis_title='Cidade', yaxis_title='Taxa de Importação (%)', template='plotly_white')
fig_bar.show()

# Gráfico de dispersão interativo para analisar a relação entre Valor Importado e Taxa de Importação
fig_scatter = px.scatter(df, 
                         x='Valor Importado (R$)', 
                         y='Taxa de Importação (%)', 
                         color='Cidade', 
                         size='Valor Importado (R$)', 
                         hover_name='Cidade',
                         title='Relação entre Valor Importado e Taxa de Importação',
                         size_max=60)

fig_scatter.update_layout(xaxis_title='Valor Importado (R$)', yaxis_title='Taxa de Importação (%)', template='plotly_white')
fig_scatter.show()