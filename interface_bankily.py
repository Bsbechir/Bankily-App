import streamlit as st
import pandas as pd
import os
from datetime import date

# Logo Bankily (le fichier doit être dans le même dossier)
st.image("bankily.JPG", width=250)

# Dictionnaire des points et agents
points_agents = {
    "Socogim": "Mahfoudh",
    "Bawadi": "Idriss",
    "Tarhil": "Ghazali",
    "Istanbul": "Meftah",
    "Kossovo": "Haroun"
}

FILENAME = "donnees_bankily.csv"

if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["Date", "Point", "Agent", "Liquidite", "Portefeuille", "Capital", "Profit"])
    df_init.to_csv(FILENAME, index=False)

st.title("Interface de saisie - Point Bankily")

date_saisie = st.date_input("Date", value=date.today())
point = st.selectbox("Point Bankily", list(points_agents.keys()))
agent = points_agents[point]
st.text_input("Agent responsable", value=agent, disabled=True)

liquidite = st.number_input("Liquidité (MRU)", min_value=0.0, format="%.2f")
portefeuille = st.number_input("Portefeuille (MRU)", min_value=0.0, format="%.2f")
profit = st.number_input("Profit journalier (MRU)", min_value=0.0, format="%.2f")

capital = liquidite + portefeuille
st.write(f"💼 Capital calculé : {capital:.2f} MRU")

if st.button("Enregistrer les données"):
    df = pd.read_csv(FILENAME)
    nouvelle_ligne = {
        "Date": date_saisie,
        "Point": point,
        "Agent": agent,
        "Liquidite": liquidite,
        "Portefeuille": portefeuille,
        "Capital": capital,
        "Profit": profit
    }
    df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
    df.to_csv(FILENAME, index=False)
    st.success("✅ Données enregistrées avec succès !")

st.subheader("📋 Données enregistrées")
df = pd.read_csv(FILENAME)
st.dataframe(df.sort_values(by="Date", ascending=False))

