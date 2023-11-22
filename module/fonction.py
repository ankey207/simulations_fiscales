import os
import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def charger_fichier(uploaded_file):
    if not os.path.exists("data"):
        os.makedirs("data")
    df = pd.read_excel(uploaded_file)
    df.to_excel('data/base.xlsx', index=False)



def dash_chef_equipe():

    # Création de données fictives
    data = pd.DataFrame({
        'Cadrant': ['Cadrant 1', 'Cadrant 2', 'Cadrant 3'],
        'Montant (€)': [500, 800, 600]
    })

    # Crée trois colonnes
    # Style personnalisé pour les cadrants
    cadrant_style = 'color: #0068c9; text-align: center; font-weight: bold; font-size: 30px;background-color: #eeeeee; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 2px #888888;'
    metric_style = 'color: #0068c9; text-align: center; font-weight: bold; font-size: 30px; background-color: #eeeeee; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 2px #888888;'

    a1, a2, a3 = st.columns(3,gap="small")
    with a1:
        st.markdown(f'<div style="{metric_style}">€ 500</div>', unsafe_allow_html=True)
        st.metric("Montant Total retiré (CFA)", 45)

    # Élément metric 2
    with a2:
        st.markdown(f'<div style="{metric_style}">€ 34556</div>', unsafe_allow_html=True)
        st.metric("Montant Total déposé", 34)

    # Élément metric 3
    with a3:
        st.markdown(f'<div style="{metric_style}">€ 790</div>', unsafe_allow_html=True)
        st.metric("Montant Total transféré", 455)