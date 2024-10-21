import streamlit as st
import st_format as sf


st.set_page_config(
    page_title="VK Digital - Conclusões",
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

sf.line(5, "blue")
sf.center_text("Conclusões", 1, "white")  
sf.line(5, "blue")

sf.text_left("1. Análise de Conversão por Canal de Origem (UTM Source)", 3, "yellow") 
st.text("")
sf.text_left("Ao analisar os dados de conversão por canal de origem (UTM Source), observamos:", 5, "white") 
st.text("")
sf.text_left("- YouTube teve uma taxa de conversão de 100% (1 lead, 1 comprador), mas isso é um valor muito pequeno para tirar conclusões concretas.", 5, "white") 
sf.text_left("- Manychat foi o canal com maior volume de leads (599 leads), resultando em 13 compradores e uma taxa de conversão de 2.17%.", 5, "white") 
sf.text_left("- STORIES teve uma taxa de conversão de 1.61% com 248 leads e 4 compradores.", 5, "white") 
st.text("")
sf.text_left("-Conclusão:", 4, "yellow")  
sf.text_left("Apesar de a taxa de conversão do YouTube ser a mais alta, o volume de leads é extremamente pequeno. Manychat, com uma maior quantidade de leads, se destacou com uma conversão acima da média. Esse é um canal que poderia receber mais investimento e melhorias em futuras campanhas, possivelmente ajustando a segmentação ou o conteúdo para aumentar ainda mais as conversões.", 5, "white") 
sf.line(5, "blue")

sf.text_left("2. Análise de Conversão por Público (UTM Medium)", 3, "yellow") 
st.text("")
sf.text_left("Ao analisar o público (Medium), observamos que:", 5, "white")  
st.text("")
sf.text_left("- O público vindo do YouTube também obteve uma conversão de 100%, com apenas 1 lead.", 5, "white") 
sf.text_left("- O público '1.00_Checkout_pagina_vendas_180D' teve 32 leads e 2 compradores, resultando em uma conversão de 6.25%, que é significativamente alta em relação aos outros canais.", 5, "white") 
sf.text_left("- Públicos lookalike_1 e lookalike_3, que são audiências similares, tiveram conversões menores, com taxas de 3.85% e 4.76%.", 5, "white") 
st.text("")
sf.text_left("-Conclusão:", 4, "yellow")  
sf.text_left("O público da página de vendas apresentaram uma taxa de conversão bastante significativa. Campanhas futuras podem explorar mais o remarketing e melhorar a segmentação de públicos lookalike para aumentar a eficiência dessas campanhas.", 5, "white") 
sf.line(5, "blue")

sf.text_left("3. Análise de Conversão por Anúncio (UTM Term)", 3, "yellow")  
st.text("")
sf.text_left("Na análise por anúncio (UTM Term):", 5, "white") 
st.text("")
sf.text_left("- O anúncio 'youtube' converteu 100% dos leads.", 5, "white") 
sf.text_left("- O anúncio 'VD_54' teve uma conversão de 16.67%, enquanto outros anúncios, como 'VD_51' e 'AD51', tiveram conversões de 10%.", 5, "white") 
st.text("")
sf.text_left("-Conclusão:", 4, "yellow") 
sf.text_left("O anúncio 'VD_54' foi o mais eficaz, seguido pelos demais com conversões notáveis. Isso indica que os anúncios focados no formato de vídeo podem ser mais impactantes, sugerindo que a criação de mais vídeos ou ajustes no formato de anúncios pode ser uma ótima estratégia para futuros lançamentos.", 5, "white") 
sf.line(5, "blue")


sf.text_left("4. Análise de Perfil Demográfico dos Compradores", 3, "yellow") 
st.text("")
sf.text_left("Cruzando os dados de idade, renda e o tempo que conhecem o expert, temos:", 5, "white") 
st.text("")
sf.text_left("- A maior parte dos compradores está na faixa etária de 31 a 60 anos, com maior concentração em 41 a 55 anos.", 5, "white") 
sf.text_left("- A maioria dos compradores tem renda de até R$ 1.500,00 ou de R$ 1.500,00 a R$ 3.000,00.", 5, "white") 
sf.text_left("- Tempo de conhecimento do expert: A maior parte dos compradores conhece o expert há menos de 1 mês ou mais de 2 anos.", 5, "white") 
st.text("")
sf.text_left("-Conclusão:", 4, "yellow") 
sf.text_left("O perfil dominante dos compradores indica que a audiência tem maior conversão entre pessoas de meia-idade, com renda baixa a média e que acabaram de conhecer o expert ou são seguidores de longa data. Uma recomendação seria criar estratégias de marketing direcionadas a esse público, com ofertas especiais para leads novos e antigos, além de ajustar o ticket médio para atrair quem tem menor poder aquisitivo.", 5, "white")  
sf.line(5, "blue")

sf.text_left("5. Análise Qualitativa dos Anúncios", 3, "yellow") 
st.text("")
sf.text_left("O quarto arquivo traz links para os anúncios de Instagram usados na campanha. Depois de ver as postagens cheguei às seguintes conclusões. ", 5, "white") 
st.text("")
sf.text_left("Vídeos que receberam mais curtidas destacam-se por características específicas. O vídeo de uma pessoa andando de bicicleta na orla da praia teve o maior engajamento, sugerindo que cenários agradáveis e dinâmicos atraem mais atenção. Vídeos com dicas práticas também foram bem recebidos, demonstrando que a entrega de informações úteis gera valor para o público. A iluminação natural e cenários agradáveis, como plantas, contribuem para um apelo visual positivo.", 5, "white")
sf.text_left("Por outro lado, vídeos com baixo engajamento, como aqueles em que pessoas falam diretamente para a câmera em ambientes comuns, podem não se destacar devido à falta de elementos visuais. Convites para eventos gratuitos e tópicos sérios, como doenças, também tiveram baixo desempenho, indicando a necessidade de otimização na abordagem.", 5, "white") 
sf.text_left("O formato de vídeo é o mais popular, com vídeos dinâmicos, dicas práticas e cenários bem cuidados mostrando maior apelo. Além disso, o uso de filtros engraçados e diálogos divertidos aumenta o engajamento, sugerindo que um tom leve e divertido ressoa bem com o público.", 5, "white")
st.text("")
sf.text_left("Conclusões e recomendações:, 4, "yellow") 
sf.text_left("1. Vídeos ao ar livre e com movimento: Apostar mais em vídeos dinâmicos, com ambientes externos, paisagens e atividades, pode melhorar o engajamento.", 5, "white")
sf.text_left("2. Cenários visualmente agradáveis: O uso de ambientes com boa iluminação e elementos naturais (como plantas) deve ser explorado, pois o visual impacta diretamente no engajamento.", 5, "white")
sf.text_left("3. Dicas práticas e conteúdos educativos: Vídeos que oferecem valor imediato, como dicas e orientações práticas, tendem a gerar mais curtidas. Estratégias de conteúdo baseadas em resolver problemas específicos podem ser altamente eficazes.", 5, "white")
sf.text_left("4. Humor e elementos divertidos: Incorporar humor, diálogos e filtros engraçados pode aumentar a acessibilidade do conteúdo e gerar mais engajamento.", 5, "white")
sf.text_left("5. Evitar vídeos com pouca produção visual: Vídeos simples, onde a pessoa fala diretamente para a câmera sem um ambiente visualmente atrativo, parecem não ter tanto apelo, especialmente se não houver algo mais envolvente ou dinâmico no conteúdo.", 5, "white")
st.text("")
st.text("")
sf.text_left("Com base nesses insights, a estratégia para futuros lançamentos pode focar em criar mais conteúdos que combinem valor prático, cenários visuais atraentes e elementos de entretenimento, como humor e filtros. Isso ajudará a melhorar o engajamento e, consequentemente, as conversões.", 5, "white")
sf.line(5, "blue")

sf.text_left("Insights e Otimizações para Próximos Lançamentos:", 3, "yellow") 

sf.text_left("1. Foco em Canais com Maior Conversão: Apesar de o YouTube ter alta conversão, a base de leads é pequena. **Manychat** foi o canal com mais volume e uma conversão considerável. Vale a pena investir mais nesse canal e otimizar campanhas de remarketing para aumentar as conversões.", 5, "white") 
sf.text_left("2. Explorar Públicos Lookalike com Melhor Segmentação: O público de remarketing teve uma excelente conversão. No entanto, os públicos lookalike não tiveram o mesmo desempenho. É recomendado fazer ajustes na criação de públicos similares, talvez utilizando dados mais refinados para criar melhores segmentações.", 5, "white") 
sf.text_left("3. Aprimoramento de Anúncios de Vídeo: Anúncios em vídeo, como o 'VD_54', tiveram uma excelente performance. A criação de novos anúncios em vídeo, com base nos insights da análise qualitativa dos anúncios, pode melhorar a taxa de conversão.", 5, "white") 
sf.text_left("4. Segmentação Demográfica Refinada: Com a maioria dos compradores entre 31 e 55 anos, com renda baixa a média, vale a pena criar campanhas de email marketing, webinars ou ofertas especiais focadas nesse grupo, com conteúdo e preços que atendam às suas necessidades.", 5, "white") 
sf.text_left("5. Acompanhamento de Leads Novos e Antigos: Como os leads que conhecem o expert há menos de 1 mês e os que conhecem há mais de 2 anos convertem mais, campanhas segmentadas para esses dois grupos podem trazer melhores resultados. Ofertas especiais de boas-vindas para novos leads e conteúdos exclusivos para seguidores antigos podem aumentar o engajamento.", 5, "white") 
st.text("")
sf.line(5, "blue")
sf.text_left("Conclusão final:", 3, "yellow")
sf.text_left("A análise forneceu uma visão clara de quais canais, públicos e anúncios foram mais eficientes, além de informações valiosas sobre o perfil demográfico dos compradores. As otimizações sugeridas, como foco em anúncios de vídeo, melhor segmentação de públicos lookalike e campanhas específicas para leads novos e antigos, podem ajudar a melhorar os resultados nos próximos lançamentos.", 5, "white") 
