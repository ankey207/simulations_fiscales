import streamlit as st
import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['fatou_dieng_ensea_2023']).generate()
print(hashed_passwords)