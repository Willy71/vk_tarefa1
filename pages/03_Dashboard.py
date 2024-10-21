import streamlit as st
import st_format as sf
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="VK Digital - Dashboard",
    page_icon="🌌",
    layout="wide"
)

# We reduced the empty space at the beginning of the streamlit
reduce_space ="""
            <style type="text/css">
            /* Remueve el espacio en el encabezado por defecto de las apps de Streamlit */
            div[data-testid="stAppViewBlockContainer"]{
                padding-top:30px;
            }
            </style>
            """
# We load reduce_space
st.html(reduce_space)


# Dados
leads = 9999
compradores = 71
conversao = (compradores / leads) * 100

# Título do app no Streamlit
sf.center_text('Análise de Conversão de Leads', 2, "white")

# Definindo as etapas do funil
etapas = ['Total de Leads', 'Total de Compradores', 'Conversão (%)']
valores = [leads, compradores, round(conversao, 2)]

# Criando o gráfico de funil com Plotly
fig = go.Figure(go.Funnel(
    y=etapas,
    x=valores,
    textinfo="value+percent previous",
    marker={"color": ["#636EFA", "#EF553B", "#00CC96"]}  # Cores do funil
))

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)

# Exibindo a taxa de conversão calculada
sf.center_text(f"Taxa de Conversão: {round(conversao, 2)}%", 4, "white")
st.subheader("")

# Dados de Conversão por Canal de Origem (utmsource)
data_source = {
    'utmsource': ['youtube', '[DIRECT]', 'manychat', '[BIO]', '[STORIES]'],
    'total_leads': [1, 13, 599, 323, 248],
    'total_compradores': [1, 1, 13, 7, 4],
    'conversion_rate': [1, 0.0769, 0.0217, 0.0217, 0.0161]
}

# Dados de Conversão por Público (utmmedium)
data_medium = {
    'utmmedium': ['youtube', '[DIRECT]', '1.00_Checkout_pagina_vendas_180D', 'lookalike_3_compras_iOS_180D_Estaticos_AD4_7', 'lookalike_1_compras_180D'],
    'total_leads': [1, 13, 32, 21, 26],
    'total_compradores': [1, 1, 2, 1, 1],
    'conversion_rate': [1, 0.0769, 0.0625, 0.0476, 0.0385]
}

# Dados de Conversão por Anúncio (utmterm)
data_term = {
    'utmterm': ['youtube', 'VD_54', 'email-convite-07-nt', 'AD51', 'VD_51'],
    'total_leads': [1, 6, 8, 10, 10],
    'total_compradores': [1, 1, 1, 1, 1],
    'conversion_rate': [1, 0.1667, 0.125, 0.1, 0.1]
}

# Transformar os dados em DataFrames
df_source = pd.DataFrame(data_source)
df_medium = pd.DataFrame(data_medium)
df_term = pd.DataFrame(data_term)

# Título no Streamlit
st.title('Análise de Conversão por Canal, Público e Anúncio')

# Gráfico 1 - Conversão por Canal de Origem (utmsource)
st.subheader('Conversão por Canal de Origem (utmsource)')
fig_source = px.bar(df_source, x='utmsource', y='conversion_rate', 
                    text='conversion_rate', title="Taxa de Conversão por Canal de Origem",
                    labels={'conversion_rate':'Taxa de Conversão', 'utmsource':'Canal de Origem'})
st.plotly_chart(fig_source)

# Gráfico 2 - Conversão por Público (utmmedium)
st.subheader('Conversão por Público (utmmedium)')
fig_medium = px.bar(df_medium, x='utmmedium', y='conversion_rate', 
                    text='conversion_rate', title="Taxa de Conversão por Público",
                    labels={'conversion_rate':'Taxa de Conversão', 'utmmedium':'Público'})
st.plotly_chart(fig_medium)

# Gráfico 3 - Conversão por Anúncio (utmterm)
st.subheader('Conversão por Anúncio (utmterm)')
fig_term = px.bar(df_term, x='utmterm', y='conversion_rate', 
                  text='conversion_rate', title="Taxa de Conversão por Anúncio",
                  labels={'conversion_rate':'Taxa de Conversão', 'utmterm':'Anúncio'})
st.plotly_chart(fig_term)


