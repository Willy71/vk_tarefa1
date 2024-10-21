import streamlit as st
import plotly.graph_objects as go

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
st.title('Análise de Conversão de Leads')

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
st.subheader(f"Taxa de Conversão: {round(conversao, 2)}%")

