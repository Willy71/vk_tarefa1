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

sf.text_left("Para realizar uma análise aprofundada com os dados fornecidos, é necessário entender o cenário do lançamento a partir de diferentes perspectivas: a origem dos leads, o perfil dos compradores, e os fatores que influenciaram as conversões. A partir disso, poderemos gerar insights acionáveis e oferecer recomendações práticas. Vamos estruturar a análise em etapas:", 4, "white") 

### 1. **Análise de Conversão por Canal de Origem (UTM Source)**

sf.text_left("Ao analisar os dados de conversão por canal de origem (UTM Source), observamos:", 4, "white") 

st.markdown("- **YouTube** teve uma taxa de conversão de **100%** (1 lead, 1 comprador), mas isso é um valor muito pequeno para tirar conclusões concretas.")
st.markdown("- **Manychat** foi o canal com maior volume de leads (599 leads), resultando em 13 compradores e uma taxa de conversão de **2.17%**.")
st.markdown("- **STORIES** teve uma taxa de conversão de **1.61%** com 248 leads e 4 compradores.")
  
sf.text_left("**Conclusão**: Apesar de a taxa de conversão do YouTube ser a mais alta, o volume de leads é extremamente pequeno. Manychat, com uma maior quantidade de leads, se destacou com uma conversão acima da média. Esse é um canal que poderia receber mais investimento e melhorias em futuras campanhas, possivelmente ajustando a segmentação ou o conteúdo para aumentar ainda mais as conversões.", 4, "white") 

### 2. **Análise de Conversão por Público (UTM Medium)**

sf.text_left("Ao analisar o público (Medium), observamos que:", 4, "white") 

st.markdown("- O público vindo do **YouTube** também obteve uma conversão de **100%**, com apenas 1 lead.")
st.markdown("- O público **"1.00_Checkout_pagina_vendas_180D"** teve 32 leads e 2 compradores, resultando em uma conversão de **6.25%**, que é significativamente alta em relação aos outros canais.")
st.markdown("- Públicos **lookalike**, que são audiências similares, tiveram conversões menores, com taxas de **3.85%** e **4.76%**.")

sf.text_left("**Conclusão**: Públicos de remarketing (como o público da página de vendas) apresentaram uma taxa de conversão bastante significativa. Campanhas futuras podem explorar mais o remarketing e melhorar a segmentação de públicos lookalike para aumentar a eficiência dessas campanhas.", 4, "white") 

sf.text_left("### 3. **Análise de Conversão por Anúncio (UTM Term)**", 4, "white") 

sf.text_left("Na análise por anúncio (UTM Term):", 4, "white") 

st.markdown("- O anúncio "youtube" converteu 100% dos leads.")
st.markdown("- O anúncio "VD_54" teve uma conversão de **16.67%**, enquanto outros anúncios, como "VD_51" e "AD51", tiveram conversões de **10%**.")

sf.text_left("**Conclusão**: O anúncio "VD_54" foi o mais eficaz, seguido pelos demais com conversões notáveis. Isso indica que os anúncios focados no formato de vídeo podem ser mais impactantes, sugerindo que a criação de mais vídeos ou ajustes no formato de anúncios pode ser uma ótima estratégia para futuros lançamentos.", 4, "white") 

sf.text_left("### 4. **Análise de Perfil Demográfico dos Compradores**", 4, "white") 

sf.text_left("Cruzando os dados de idade, renda e o tempo que conhecem o expert, temos:", 4, "white") 

st.markdown("- A maior parte dos compradores está na faixa etária de **31 a 60 anos**, com maior concentração em **41 a 55 anos**.")
st.markdown("- A maioria dos compradores tem renda de **até R$ 1.500,00** ou **de R$ 1.500,00 a R$ 3.000,00**.")
st.markdown("- **Tempo de conhecimento** do expert: A maior parte dos compradores conhece o expert há **menos de 1 mês** ou **mais de 2 anos**.")

sf.text_left("**Conclusão**: O perfil dominante dos compradores indica que a audiência tem maior conversão entre pessoas de meia-idade, com renda baixa a média e que acabaram de conhecer o expert ou são seguidores de longa data. Uma recomendação seria criar estratégias de marketing direcionadas a esse público, com ofertas especiais para leads novos e antigos, além de ajustar o ticket médio para atrair quem tem menor poder aquisitivo.", 4, "white") 

sf.text_left("### 5. **Análise Qualitativa dos Anúncios**", 4, "white") 

sf.text_left("O **quarto arquivo** traz links para os anúncios usados na campanha. Esses dados podem ser analisados qualitativamente para verificar quais elementos criativos e de mensagem estão mais alinhados com os públicos que tiveram maiores conversões.", 4, "white") 

sf.text_left("**Conclusão**: A análise qualitativa pode focar em identificar padrões criativos, como cores, tom de voz, ou elementos visuais que geraram mais engajamento, e replicar essas boas práticas nos futuros anúncios. Além disso, ajustar anúncios que não geraram bons resultados pode melhorar o ROI.", 4, "white") 

sf.line(5, "blue")

sf.text_left("## Insights e Otimizações para Próximos Lançamentos:", 4, "white") 

st.markdown("1. **Foco em Canais com Maior Conversão**: Apesar de o YouTube ter alta conversão, a base de leads é pequena. **Manychat** foi o canal com mais volume e uma conversão considerável. Vale a pena investir mais nesse canal e otimizar campanhas de remarketing para aumentar as conversões.")
   
st.markdown("2. **Explorar Públicos Lookalike com Melhor Segmentação**: O público de remarketing teve uma excelente conversão. No entanto, os públicos lookalike não tiveram o mesmo desempenho. É recomendado fazer ajustes na criação de públicos similares, talvez utilizando dados mais refinados para criar melhores segmentações.")

st.markdown("3. **Aprimoramento de Anúncios de Vídeo**: Anúncios em vídeo, como o "VD_54", tiveram uma excelente performance. A criação de novos anúncios em vídeo, com base nos insights da análise qualitativa dos anúncios, pode melhorar a taxa de conversão.")

st.markdown("4. **Segmentação Demográfica Refinada**: Com a maioria dos compradores entre 31 e 55 anos, com renda baixa a média, vale a pena criar campanhas de email marketing, webinars ou ofertas especiais focadas nesse grupo, com conteúdo e preços que atendam às suas necessidades.")

st.markdown("5. **Acompanhamento de Leads Novos e Antigos**: Como os leads que conhecem o expert há menos de 1 mês e os que conhecem há mais de 2 anos convertem mais, campanhas segmentadas para esses dois grupos podem trazer melhores resultados. Ofertas especiais de boas-vindas para novos leads e conteúdos exclusivos para seguidores antigos podem aumentar o engajamento.")

sf.text_left("### Conclusão Final:", 4, "white") 
sf.text_left("A análise forneceu uma visão clara de quais canais, públicos e anúncios foram mais eficientes, além de informações valiosas sobre o perfil demográfico dos compradores. As otimizações sugeridas, como foco em anúncios de vídeo, melhor segmentação de públicos lookalike e campanhas específicas para leads novos e antigos, podem ajudar a melhorar os resultados nos próximos lançamentos.", 4, "white") 
