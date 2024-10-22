import streamlit as st
import st_format as sf
import pandas as pd

st.set_page_config(
    page_title="VK Digital - Resolução das tarefas",
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


sf.text_left("Para montar um estudo com base nos dados fornecidos, vou estruturar o análise em três grandes etapas:", 4, "white")

sf.text_left("Análise de Inscrição e Captação de Leads:", 4, "yellow")
sf.text_left("Avaliação dos leads inscritos por meio da primeira tabela ('001_TabelaPesquisaUTMsn.csv'), com destaque para os canais de origem (source), tipo de tráfego (medium) e anúncios (term) que mais geraram leads.", 6, "lightgrey")

sf.text_left("Análise de Conversão de Leads para Compradores:", 4, "yellow")
sf.text_left("Cruzamento dos dados de leads com os compradores da segunda tabela ('002_TabelaVendas.csv') para identificar taxas de conversão por canal, tráfego e anúncio. Isso pode indicar quais estratégias geraram mais vendas.", 6, "lightgrey")

sf.text_left("Perfil dos Leads e Compradores:", 4, "yellow")
sf.text_left("Com base na pesquisa de persona (terceira tabela, '003_TabelaPesquisa.csv'), analisare o perfil dos leads que responderam a pesquisa, verificando idade, renda e há quanto tempo conhecem o expert. Cruzar esses dados com os compradores também pode fornecer insights sobre o perfil dos clientes que compraram.", 6, "lightgrey")

sf.text_left("Passos:", 4, "yellow")
with st.container():
  col01, col02 = st.columns([0.5,6]) 
  with col02:
    st.markdown("Carregar os dados das quatro tabelas.")
    st.markdown("Explorar e cruzar os dados para gerar insights sobre:")
    with st.container():
      col03, col04 = st.columns([0.5,6]) 
      with col04:
        st.markdown("Distribuição de leads por canal e tráfego.")
        st.markdown("Taxa de conversão por canal/anúncio.")
        st.markdown("Perfis demográficos dos leads e compradores.")

st.text("")    
sf.text_left("Vou iniciar carregando e analisando os dados das quatro tabelas.", 5,"lightgrey")
st.text("")
code_01 = '''import pandas as pd

# Carregar as quatro tabelas de dados
path_leads = '/data/001_TabelaPesquisaUTMsn.csv'
path_vendas = '/data/002_TabelaVendas.csv'
path_pesquisa = '/data/003_TabelaPesquisa.csv'
path_qualidade = '/data/004_TabelaAdsLinks.csv'

# Lendo os arquivos CSV
leads_df = pd.read_csv(path_leads)
vendas_df = pd.read_csv(path_vendas)
pesquisa_df = pd.read_csv(path_pesquisa)
qualidade_df = pd.read_csv(path_qualidade)

# Exibir as primeiras linhas de cada tabela para revisão
st.dataframe(leads_df.head(), hide_index=True, column_config={leads_df.columns[0] : None})
st.dataframe(vendas_df.head(), hide_index=True, column_config={vendas_df.columns[0] : None})
st.dataframe(pesquisa_df.head(), hide_index=True, column_config={pesquisa_df.columns[0] : None})
st.dataframe(qualidade_df.head(), hide_index=True)
")
'''
st.code(code_01, language="python")

path_leads = 'data/001_TabelaPesquisaUTMsn.csv'
path_vendas = 'data/002_TabelaVendas.csv'
path_pesquisa = 'data/003_TabelaPesquisa.csv'
path_qualidade = 'data/004_TabelaAdsLinks.csv'

leads_df = pd.read_csv(path_leads)
vendas_df = pd.read_csv(path_vendas)
pesquisa_df = pd.read_csv(path_pesquisa)
qualidade_df = pd.read_csv(path_qualidade)

st.dataframe(leads_df.head(), hide_index=True, column_config={leads_df.columns[0] : None})
st.dataframe(vendas_df.head(), hide_index=True, column_config={vendas_df.columns[0] : None})
st.dataframe(pesquisa_df.head(), hide_index=True, column_config={pesquisa_df.columns[0] : None})
st.dataframe(qualidade_df.head(), hide_index=True)
st.text("")

sf.text_left("Aqui está um resumo das quatro tabelas:", 4, "white")

sf.text_left("1 - Tabela de Leads (Inscritos):", 4, "yellow")
with st.container():
  col05, col06 = st.columns([0.5,6]) 
  with col06:
    sf.text_left("Colunas principais:", 4, "lightgrey")
    with st.container():
      col07, col08 = st.columns([0.5,6]) 
      with col08:
        st.markdown("email: E-mail do lead.")
        st.markdown("utmsource: Canal de origem do lead (ex: 'facebookads').")
        st.markdown("utmmedium: Público do tráfego pago (ex: 'lookalike_1_compras_180D').")
        st.markdown("utmterm: Anúncio específico que trouxe o lead (ex: 'AD17').")

sf.text_left("2 - Tabela de Vendas (Compradores):", 4, "yellow")
with st.container():
  col09, col10 = st.columns([0.5,6]) 
  with col10:
    sf.text_left("Coluna principal:", 4, "lightgrey")
    with st.container():
      col11, col12 = st.columns([0.5,6]) 
      with col12:
        st.markdown("email: E-mail do comprador.")



sf.text_left("3 - Tabela de Pesquisa (Perfil de Leads):", 4, "yellow")
with st.container():
  col13, col14 = st.columns([0.5,6]) 
  with col14:
    sf.text_left("Colunas principais:", 4, "lightgrey")
    with st.container():
      col15, col16 = st.columns([0.5,6]) 
      with col16:
        st.markdown("email: E-mail do lead que respondeu a pesquisa.")
        st.markdown("idade: Faixa etária do lead.")
        st.markdown("renda: Faixa de renda do lead.")
        st.markdown("tempo_me_conhece: Tempo que o lead conhece o expert.")

sf.text_left("4 - Tabela de Qualidade:", 4, "yellow")
with st.container():
  col13, col14 = st.columns([0.5,6]) 
  with col14:
    sf.text_left("Colunas principais:", 4, "lightgrey")
    with st.container():
      col15, col16 = st.columns([0.5,6]) 
      with col16:
        st.markdown("utmterm: Anúncio específico que trouxe o lead (ex: 'AD17').")
        st.markdown("instagram_permalink_url: Anúncio de instagram")

sf.line(5, "blue")

sf.text_left("Próximos passos:", 4, "yellow")
with st.container():
  col17, col18 = st.columns([0.5,6]) 
  with col18:
    st.markdown("Identificar quais leads da tabela de inscritos (leads_df) realizaram compras, cruzando com a tabela de vendas (vendas_df).")
    st.markdown("Vou analisar o perfil dos leads (pesquisa_df) e verificar se há alguma correlação com as conversões.")
st.text("")

sf.text_left("Vou realizar a análise de conversão de leads para compradores.", 4, "white")

code_02 = '''
# Cruzar leads com compradores
# Verificar quais emails da tabela de vendas aparecem na tabela de leads

# Adicionando uma coluna de "comprador" à tabela de leads (1 para quem comprou, 0 para quem não comprou)
leads_df['comprador'] = leads_df['email'].isin(vendas_df['email']).astype(int)

# Ver quantos leads se converteram em compradores
conversion_rate = leads_df['comprador'].mean()

# Contar o número total de leads e compradores
total_leads = len(leads_df)
total_compradores = leads_df['comprador'].sum()

sf.text_left(f"Total de leads:{total_leads}", 5, "white")
sf.text_left(f"Total de compradores:{total_compradores}", 5, "white")
sf.text_left(f"Conversão: {(conversion_rate*100):.2f}%", 5, "white")
'''
st.code(code_02, language="python")
# Adicionando uma coluna de "comprador" à tabela de leads (1 para quem comprou, 0 para quem não comprou)
leads_df['comprador'] = leads_df['email'].isin(vendas_df['email']).astype(int)
# Ver quantos leads se converteram em compradores
conversion_rate = leads_df['comprador'].mean()
# Contar o número total de leads e compradores
total_leads = len(leads_df)
total_compradores = leads_df['comprador'].sum()

sf.text_left(f"Total de leads:{total_leads}", 5, "white")
sf.text_left(f"Total de compradores:{total_compradores}", 5, "white")
sf.text_left(f"Conversão:\t\t\t{(conversion_rate*100):.2f}%", 5, "white")

st.text("")

sf.text_left("Agora, vou detalhar a análise por canal de origem (utmsource), público (utmmedium), e anúncio (utmterm) para identificar quais estratégias de marketing trouxeram mais compradores.", 4, "white")

code_03 = '''
# Analisar a taxa de conversão por canal (utmsource), público (utmmedium) e anúncio (utmterm)

# Taxa de conversão por canal de origem (utmsource)
conversion_by_source = leads_df.groupby('utmsource')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_source.columns = ['utmsource', 'total_leads', 'total_compradores', 'conversion_rate']

# Taxa de conversão por público (utmmedium)
conversion_by_medium = leads_df.groupby('utmmedium')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_medium.columns = ['utmmedium', 'total_leads', 'total_compradores', 'conversion_rate']

# Taxa de conversão por anúncio (utmterm)
conversion_by_term = leads_df.groupby('utmterm')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_term.columns = ['utmterm', 'total_leads', 'total_compradores', 'conversion_rate']

conversion_by_source.sort_values(by='conversion_rate', ascending=False).head(), conversion_by_medium.sort_values(by='conversion_rate', ascending=False).head(), conversion_by_term.sort_values(by='conversion_rate', ascending=False).head()
'''

st.code(code_03, language="python")

# Analisar a taxa de conversão por canal (utmsource), público (utmmedium) e anúncio (utmterm)

# Taxa de conversão por canal de origem (utmsource)
conversion_by_source = leads_df.groupby('utmsource')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_source.columns = ['utmsource', 'total_leads', 'total_compradores', 'conversion_rate']

# Taxa de conversão por público (utmmedium)
conversion_by_medium = leads_df.groupby('utmmedium')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_medium.columns = ['utmmedium', 'total_leads', 'total_compradores', 'conversion_rate']

# Taxa de conversão por anúncio (utmterm)
conversion_by_term = leads_df.groupby('utmterm')['comprador'].agg(['count', 'sum', 'mean']).reset_index()
conversion_by_term.columns = ['utmterm', 'total_leads', 'total_compradores', 'conversion_rate']

st.write(conversion_by_source.sort_values(by='conversion_rate', ascending=False).head())
st.write(conversion_by_medium.sort_values(by='conversion_rate', ascending=False).head())
st.write(conversion_by_term.sort_values(by='conversion_rate', ascending=False).head())

st.text("")
sf.text_left("Aqui estão as principais descobertas relacionadas às conversões por canal, público e anúncio:", 4, "white")

sf.text_left("Conversão por Canal de Origem (utmsource):", 4, "yellow")
with st.container():
  col19, col20 = st.columns([0.5,6]) 
  with col20:
    st.markdown("youtube: 1 lead com 100% de conversão.")
    st.markdown("[DIRECT]: 13 leads, 1 comprador, taxa de conversão de 7,69%.")
    st.markdown("manychat: 599 leads, 13 compradores, taxa de conversão de 2,17%.")
    st.markdown("[BIO]: 323 leads, 7 compradores, taxa de conversão de 2,17%.")


sf.text_left("Conversão por Público (utmmedium):", 4, "yellow")
with st.container():
  col21, col22 = st.columns([0.5,6]) 
  with col22:
    st.markdown("youtube: 1 lead com 100% de conversão.")
    st.markdown("[DIRECT]: 13 leads, 1 comprador, taxa de conversão de 7,69%.")
    st.markdown("1.00_Checkout_pagina_vendas_180D: 32 leads, 2 compradores, taxa de conversão de 6,25%.")
    st.markdown("lookalike_3_compras_iOS_180D_Estaticos_AD4_7: 21 leads, 1 comprador, taxa de conversão de 4,76%.")


sf.text_left("Conversão por Anúncio (utmterm):", 4, "yellow")
with st.container():
  col23, col24 = st.columns([0.5,6]) 
  with col24:
    st.markdown("youtube: 1 lead com 100% de conversão.")
    st.markdown("VD_54: 6 leads, 1 comprador, taxa de conversão de 16,67%.")
    st.markdown("email-convite-07-nt: 8 leads, 1 comprador, taxa de conversão de 12,5%.")

sf.line(5, "blue")
sf.text_left("Próximos passos:", 4, "yellow")
st.text("")
sf.text_left("Agora, vou cruzar os dados da pesquisa (idade, renda, tempo que conhecem o expert) com as conversões para entender melhor o perfil dos compradores e gerar possíveis otimizações.", 4, "lightgrey")

code_04 = '''
# Cruzar os dados de pesquisa com os dados de leads (incluindo informação de compradores)
# Vamos unir as tabelas de leads e pesquisa com base no e-mail

leads_pesquisa_df = pd.merge(leads_df, pesquisa_df, on='email', how='left')

# Verificar o perfil demográfico dos compradores
compradores_df = leads_pesquisa_df[leads_pesquisa_df['comprador'] == 1]

# Resumir perfil dos compradores (idade, renda, tempo de conhecimento)
perfil_compradores = compradores_df[['idade', 'renda', 'tempo_me_conhece']].value_counts().reset_index(name='count')

perfil_compradores.sort_values(by='count', ascending=False).head()
'''

st.code(code_04, language="python")

st.text("")

# Cruzar os dados de pesquisa com os dados de leads (incluindo informação de compradores)
# Vamos unir as tabelas de leads e pesquisa com base no e-mail

leads_pesquisa_df = pd.merge(leads_df, pesquisa_df, on='email', how='left')

# Verificar o perfil demográfico dos compradores
compradores_df = leads_pesquisa_df[leads_pesquisa_df['comprador'] == 1]

# Resumir perfil dos compradores (idade, renda, tempo de conhecimento)
perfil_compradores = compradores_df[['idade', 'renda', 'tempo_me_conhece']].value_counts().reset_index(name='count')

perfil_compradores.sort_values(by='count', ascending=False).head()

st.write(perfil_compradores)


