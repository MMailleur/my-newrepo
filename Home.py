import streamlit as st  # Importation du module Streamlit pour créer l'application web
import requests  # Importation du module requests pour effectuer des requêtes HTTP
import random  # Importation du module random pour générer des nombres aléatoires
from streamlit_extras.let_it_rain import rain  # Importation d'une librairie externe

st.set_page_config(
    page_title="FakeNews",  # Configuration du titre de la page
    page_icon=":newspaper:",  # Configuration de l'icône de la page
)

@st.cache_data
def get_data(label, lengthtext, nbrow):
    return requests.get(f"https://appfake.azurewebsites.net/data/?label={label}&lengthtext={lengthtext}&nbrow={nbrow}").json()

def stem_get_data(lengthtext, nbrow):
    return requests.get(f"https://appfake.azurewebsites.net/datastem/?lengthtext={lengthtext}&nbrow={nbrow}").json()

data_true = get_data(0, 150, 10)  # Récupération des données de vraies nouvelles
data_false = get_data(1, 150, 10)  # Récupération des données de fausses nouvelles
stemdata = stem_get_data(100, 10)  # Récupération des données traitées

st.title("What is a :red[Fake news]?")  # Affichage du titre de l'application

st.markdown(
    """
    <style>
    .title-wrapper {
        position: relative;
        background-color: black;
        padding: 10px;
    }
    .title-wrapper span {
        position: relative;
        color: white;
        z-index: 1;
        font-size: 30px !important;
    }
    .title-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: black;
        z-index: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title-wrapper"><span>Fake news is false or misleading information presented as news.\
    Fake news often has the aim of damaging the reputation of a person or entity, or making money through advertising revenue. Although false news has always been spread throughout history, the term "fake news" was first used in the 1890s when sensational reports in newspapers were common</span></div>', unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/02/21/10/55/paper-planes-4011071_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()  # Appel de la fonction pour ajouter l'arrière-plan à l'application
