import streamlit as st
import st_format as sf

sf.text_left("Nossa ideia é te inserir num ambiente prático que você viverá e te dar liberdade para fazer o melhor que você que conseguir, independente do que for.", 4, "white")

st.text("")


sf.text_left("Analisaremos:", 4, "white")
with st.container():
  col01, col02 = st.columns([0.5,6]) 
  with col01:
    sf.text_left("- Se sua análise de fato se transformou em insights úteis para o lançamento", 5, 'lightgrey')
    sf.text_left("- Quanto as conclusões geradas dos dados estavam corretas", 5, 'lightgrey')
    sf.text_left("- Quanto capricho visual e organizacional você trouxe", 5, 'lightgrey')
    sf.text_left("- Quão bem você argumentou sobre os pontos que trouxe", 5, 'lightgrey')
    sf.text_left("- Quão profundo e criativo você foi em sua análise", 5, 'lightgrey')


st.text("")

sf.text_left("Segue a descrição e link para as tabelas.", 4, "white")
sf.text_left("A primeira tabela de dados traz dados de leads inscritos em um lançamento, ou seja, dados de quem se inscreveu para participar de um lançamento.", 4, "white")
sf.text_left("Na tabela há o e-mail do lead e os parâmetros de UTM de entrada desse lead. Dica: UTMs são parâmetros que indicam a origem do lead, nesse caso, Source representa o canal de origem, Medium (para canais de tráfego pago) representa o público e Term (para canais de tráfego pago) o anúncio que trouxe o lead.", 4, "white")
