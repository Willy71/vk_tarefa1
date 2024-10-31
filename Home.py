import streamlit as st
import st_format as sf

st.set_page_config(
    page_title="VK Digital - Trabalho 1",
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

st.header("")
st.header("")
sf.center_picture("https://github.com/Willy71/vk_tarefa1/blob/main/picture/Marketing.png?raw=true", 400)

#sf.line(5, "blue")
#sf.center_text("Análise de BI e planejamento estratégico para lançamento de produtos digitais.", 2, "lightgrey")
#sf.line(5, "blue")


