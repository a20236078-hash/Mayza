import streamlit as st

st.set_page_config(page_title="Pregunta para ti 🤔", page_icon="❓", layout="centered")

# Título
st.markdown("<h2 style='text-align: center; color: black;'>¿Te caigo bien?</h2>", unsafe_allow_html=True)

# Botones de respuesta
col1, col2 = st.columns(2)

with col1:
    if st.button("Sí 👍"):
        st.success("¡Gracias! Tú también me caes genial 😎")

with col2:
    if st.button("No 👎"):
        st.warning("En 2026 hablamos, bye 👋")


