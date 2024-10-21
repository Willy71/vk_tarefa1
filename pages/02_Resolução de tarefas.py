import streamlit as st
import st_format as sf


sf.text_left("Para montar um estudo com base nos dados fornecidos, podemos estruturar a análise em três grandes etapas:", 4, "white")

sf.text_left("Análise de Inscrição e Captação de Leads:", 4, "lighorange")
sf.text_left("Avaliação dos leads inscritos por meio da primeira tabela ('001_TabelaPesquisaUTMsn.csv'), com destaque para os canais de origem (source), tipo de tráfego (medium) e anúncios (term) que mais geraram leads.", 5, "lightgrey")

sf.text_left("Análise de Conversão de Leads para Compradores:", 4, "white")
sf.text_left("Cruzamento dos dados de leads com os compradores da segunda tabela ('002_TabelaVendas.csv') para identificar taxas de conversão por canal, tráfego e anúncio. Isso pode indicar quais estratégias geraram mais vendas.", 5, "lightgrey")

sf.text_left("Perfil dos Leads e Compradores:", 4, "white")
sf.text_left("Com base na pesquisa de persona (terceira tabela, '003_TabelaPesquisa.csv'), analisaremos o perfil dos leads que responderam a pesquisa, verificando idade, renda e há quanto tempo conhecem o expert. Cruzar esses dados com os compradores também pode fornecer insights sobre o perfil dos clientes que compraram.", 5, "lightgrey")

sf.text_left("Passos:", 4, "white")
sf.text_left("Carregar os dados das três tabelas.", 4, "white")
sf.text_left("Explorar e cruzar os dados para gerar insights sobre:", 4, "white")
sf.text_left("Distribuição de leads por canal e tráfego.", 4, "white")
sf.text_left("Taxa de conversão por canal/anúncio.", 4, "white")
sf.text_left("Perfis demográficos dos leads e compradores.", 4, "white")
sf.text_left("Vou iniciar carregando e analisando os dados das três tabelas.", 4, "white")
