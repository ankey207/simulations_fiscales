from pathlib import Path
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu
import os
from module import fonction
st.set_page_config(page_title="Simulation Revenu", page_icon="favicon.jpg")

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# load hashed passwords
file_path = Path(__file__).parent / "config.yaml"
with file_path.open("rb") as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
authenticator.login('Connexion', 'main')

if st.session_state["authentication_status"]:
	authenticator.logout('Deconnexion', 'sidebar', key='unique_key')
	user = st.session_state['name']
	if st.session_state['name'] == 'super_admin':
		user = 'admin'
	default_index = ["chef_equipe","superviseur","admin"].index(user)
	with st.sidebar:
		selected = option_menu( 
			menu_title="Menu",
			options=[ "Policy choices", "Results", "How it works"],
			icons=['gear', 'columns-gap', "question-octagon-fill"], 
    		menu_icon="cast",
			default_index=0
		)
	if selected == "Policy choices":
		z1, z2 = st.columns(2)
		with z1:
		    st.title(":blue[Choisissez le fichier de données:]")
		with z2:
			uploaded_file = st.file_uploader(":blue[Choisir le fichier de données:]",accept_multiple_files=False,type=["xls", "xlsx"],label_visibility='hidden')
		if uploaded_file is not None:
			fonction.charger_fichier(uploaded_file)

		nb_choix_politique = st.slider('Nombre de choix de politiques', 1, 3, 1)
		income_tax, Direct_transfer_rules, VAT_rules, Rules_on_indirect_transfers = st.tabs(["Income tax", "Direct transfer rules", "VAT rules","Rules on indirect transfers (health and education)"])
		with income_tax:
			st.title(f"Nous sommes sur la page income_tax ")
		with Direct_transfer_rules:
			st.title(f"Nous sommes sur la page Direct_transfer_rules")
		with VAT_rules:
			st.title(f"Nous sommes sur la page VAT_rules")
		with Rules_on_indirect_transfers:
			st.title(f"Nous sommes sur la page Rules_on_indirect_transfers")
		    

	elif selected == "Results":
		st.title(f"Nous sommes sur la page {selected}")
	elif selected == "How it works":
		st.title("How works this application ?")
		st.write("The ultimate goal is to enable users to understand and analyze the effects of various fiscal policies by visualizing their impact on income and tax distribution.")
		
elif st.session_state["authentication_status"] is False:
    st.error('Le login ou le mot de passe est incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez entrer votre login et votre mot de passe')


footer="""<style>
    a:link , a:visited{
    color: blue;
    background-color: transparent;
    text-decoration: underline;
    }

    a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
    }

    .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    }
</style>
<div class="footer">
    <p>Developed with🧡by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/nsi%C3%A9ni-kouadio-eli%C3%A9zer-amany-613681185" target="_blank">Nsiéni Amany Kouadio</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

