import streamlit as st
import st_format as sf
import pandas as pd


sf.text_left("Para montar um estudo com base nos dados fornecidos, podemos estruturar a análise em três grandes etapas:", 4, "white")

sf.text_left("Análise de Inscrição e Captação de Leads:", 4, "yellow")
sf.text_left("Avaliação dos leads inscritos por meio da primeira tabela ('001_TabelaPesquisaUTMsn.csv'), com destaque para os canais de origem (source), tipo de tráfego (medium) e anúncios (term) que mais geraram leads.", 6, "lightgrey")

sf.text_left("Análise de Conversão de Leads para Compradores:", 4, "yellow")
sf.text_left("Cruzamento dos dados de leads com os compradores da segunda tabela ('002_TabelaVendas.csv') para identificar taxas de conversão por canal, tráfego e anúncio. Isso pode indicar quais estratégias geraram mais vendas.", 6, "lightgrey")

sf.text_left("Perfil dos Leads e Compradores:", 4, "yellow")
sf.text_left("Com base na pesquisa de persona (terceira tabela, '003_TabelaPesquisa.csv'), analisaremos o perfil dos leads que responderam a pesquisa, verificando idade, renda e há quanto tempo conhecem o expert. Cruzar esses dados com os compradores também pode fornecer insights sobre o perfil dos clientes que compraram.", 6, "lightgrey")

sf.text_left("Passos:", 4, "yellow")
with st.container():
  col01, col02 = st.columns([0.5,6]) 
  with col02:
    st.markdown("Carregar os dados das três tabelas.")
    st.markdown("Explorar e cruzar os dados para gerar insights sobre:")
    with st.container():
      col03, col04 = st.columns([0.5,6]) 
      with col04:
        st.markdown("Distribuição de leads por canal e tráfego.")
        st.markdown("Taxa de conversão por canal/anúncio.")
        st.markdown("Perfis demográficos dos leads e compradores.")

st.text("")    
sf.text_left("Vou iniciar carregando e analisando os dados das três tabelas.", 5,"lightgrey")
st.text("")
code_01 = '''import pandas as pd

# Carregar as três tabelas de dados
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
leads_df.head(), vendas_df.head(), pesquisa_df.head(), qualidade_df.head())
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

st.write(leads_df.head(), index_col=False)
st.write(vendas_df.head(), index_col=False)
st.write(pesquisa_df.head(), index_col=False)
st.write(pesquisa_df.head(), index_col=False)



