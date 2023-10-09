import streamlit as st

# URL de la imagen que deseas mostrar
url_imagen = "//images.igdb.com/igdb/image/upload/t_thumb/co1wyy.jpg"

# Usar st.image para mostrar la imagen desde la URL
st.image(url_imagen, caption='Imagen de ejemplo', use_column_width=True)
