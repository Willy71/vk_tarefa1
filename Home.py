import streamlit as st
import st_format as sf

st.set_page_config(
    page_title="Silvertech - Trabajo final",
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
sf.center_text("Tarefa 1 para VK", 2, "lightgrey")
sf.line(5, "blue")


