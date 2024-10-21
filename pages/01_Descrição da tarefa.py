import streamlit as st
import st_format as sf

sf.text_left("Nossa ideia é te inserir num ambiente prático que você viverá e te dar liberdade para fazer o melhor que você que conseguir, independente do que for.", 4, "white")

st.text("")


sf.text_left("Analisaremos:", 4, "white")
with st.container():
  col01, col02 = st.columns([0.5,6]) 
  with col02:
    sf.text_left("- Se sua análise de fato se transformou em insights úteis para o lançamento", 5, 'lightgrey')
    sf.text_left("- Quanto as conclusões geradas dos dados estavam corretas", 5, 'lightgrey')
    sf.text_left("- Quanto capricho visual e organizacional você trouxe", 5, 'lightgrey')
    sf.text_left("- Quão bem você argumentou sobre os pontos que trouxe", 5, 'lightgrey')
    sf.text_left("- Quão profundo e criativo você foi em sua análise", 5, 'lightgrey')


st.text("")

sf.text_left("Segue a descrição e link para as tabelas.", 4, "white")
sf.text_left("A primeira tabela de dados traz dados de leads inscritos em um lançamento, ou seja, dados de quem se inscreveu para participar de um lançamento.", 4, "white")
sf.text_left("Na tabela há o e-mail do lead e os parâmetros de UTM de entrada desse lead. Dica: UTMs são parâmetros que indicam a origem do lead, nesse caso, Source representa o canal de origem, Medium (para canais de tráfego pago) representa o público e Term (para canais de tráfego pago) o anúncio que trouxe o lead.", 4, "white")

sf.left_text_link("001_TabelaPesquisaUTMsn.csv", "https://drive.google.com/file/d/1volT93MoYgn6MvC5UzWwEN3fLQIoFLsB/view?usp=sharing", 5, "white")

sf.text_left("A segunda tabela traz dados de compradores do lançamento.", 4, "white")
sf.text_left("Ela é composta apenas pelo e-mail de quem comprou a oferta realizada no lançamento.", 4, "white")

sf.left_text_link("002_TabelaVendas.csv","https://drive.google.com/file/d/1ycy2ChfmycwoyqXvbdzpq3SiiEmeZD6q/view?usp=sharing", 5, "white")

sf.text_left("A terceira tabela traz dados de uma pesquisa de persona distribuída durante a captação e que foi respondida por alguns dos leads dando mais informações sobre eles.", 4, "white")
sf.text_left("Ela é composta apenas pelo e-mail do lead que respondeu, idade, renda e há quanto tempo conhece o expert.", 4, "white")

sf.left_text_link("003_TabelaPesquisa.csv","https://drive.google.com/file/d/1C8St7Fp9SWXRogMlZ7L8bc8mHabEWzNi/view?usp=sharing", 5, "white")

sf.text_left("A quarta tabela contém o link pra alguns dos anúncios retratados como origem dos leads.", 4, "white")
sf.text_left("O anúncio em si pode servir para análises mais qualitativas do seu estudo.", 4, "white")

sf.left_text_link("004_TabelaAdsLinks.csv","https://drive.google.com/file/d/1tlXqjjj9B0mzNnIu7wXmlC4HNAm26Gvc/view?usp=sharing", 5, "white")

sf.text_left("Imagine que você está numa equipe de BI desse projeto. Com base nos dados coletados, monte um estudo que dê uma visão clara dos resultados do lançamento para os stakeholders e que também já levante possíveis otimizações para melhora de resultado em próximos lançamentos.", 4, "white")
