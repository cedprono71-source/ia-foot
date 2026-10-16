
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Foot IA",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ FOOT IA")
st.subheader("Analyse intelligente des matchs de football")

st.write(
    "Importe une capture d'écran de tes matchs "
    "pour commencer l'analyse."
)

capture = st.file_uploader(
    "📸 Choisir une capture d'écran",
    type=["png", "jpg", "jpeg"]
)

if capture is not None:
    image = Image.open(capture)
    st.image(image, caption="Capture importée", use_container_width=True)

st.divider()

st.header("📊 Analyse du match")

equipe1 = st.text_input("Équipe à domicile")
equipe2 = st.text_input("Équipe à l'extérieur")

if st.button("🔍 Analyser le match"):
    if equipe1.strip() and equipe2.strip():
        st.subheader(f"{equipe1} - {equipe2}")
        st.info(
            "Prochaine étape : ajouter les statistiques, "
            "les probabilités 1N2, les buts et les scores possibles."
        )
    else:
        st.warning("Entre le nom des deux équipes.")
