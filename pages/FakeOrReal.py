import streamlit as st  # Importation du module Streamlit pour créer l'application web
import random  # Importation du module random pour générer des nombres aléatoires
from Home import data_false, data_true  # Importation des données de fausses et vraies nouvelles

# Vérification et initialisation des variables d'état
if 'label' not in st.session_state:
    st.session_state['label'] = random.getrandbits(1)  # Attribution aléatoire de 0 ou 1 à la variable 'label'
if 'randint' not in st.session_state:
    st.session_state['randint'] = random.randint(0, 5)  # Attribution d'un nombre aléatoire entre 0 et 5 à 'randint'
if 'bouton' not in st.session_state:
    st.session_state['bouton'] = True  # Initialisation de la variable 'bouton' à True
if 'goodanswer' not in st.session_state:
    st.session_state['goodanswer'] = 0  # Initialisation du nombre de bonnes réponses à 0
if 'totanswer' not in st.session_state:
    st.session_state['totanswer'] = 0  # Initialisation du nombre total de réponses à 0

# Fonction pour générer une nouvelle question aléatoire
def new_rand():
    st.session_state['bouton'] = True  # Réinitialisation de 'bouton' à True
    st.session_state['label'] = random.getrandbits(1)  # Attribution aléatoire de 0 ou 1 à 'label'
    st.session_state['randint'] = random.randint(0, 9)  # Attribution d'un nouveau nombre aléatoire à 'randint'

col01, col02, col03 = st.columns([6, 1, 4])  # Création de colonnes pour la mise en page
with col01:
    st.title(":red[Fake news] or not ?")  # Affichage du titre de l'application
with col03:
    st.markdown('#')
    if st.button("Another news"):  # Affichage du bouton "Another news"
        new_rand()  # Appel de la fonction pour générer une nouvelle question aléatoire
        st.experimental_rerun()  # Actualisation de la page

col1, col2, col3 = st.columns([6, 1, 4])  # Création de nouvelles colonnes pour la mise en page
with col3:
    if st.session_state.totanswer > 0:
        st.header(f"Good answer {st.session_state.goodanswer}/{st.session_state.totanswer}")  # Affichage des statistiques de l'utilisateur
        st.header("What do you :red[think] ?")

    if st.session_state.label == 0:
        label_val = data_true["items"][st.session_state.randint][4]  # Récupération de la valeur attendue pour la question vraie
    else:
        label_val = data_false["items"][st.session_state.randint][4]  # Récupération de la valeur attendue pour la question fausse

    col11, col22 = st.columns(2)  # Création de deux nouvelles colonnes

    with col11:
        if st.session_state['bouton']:
            if st.button("Not Fake"):  # Affichage du bouton "Not Fake"
                if label_val == 0:
                    st.write("su")  # Affichage d'un message de confirmation pour une bonne réponse
                    st.session_state.totanswer += 1  # Incrémentation du nombre total de réponses
                    st.session_state.goodanswer += 1  # Incrémentation du nombre de bonnes réponses
                else:
                    st.write("wrong")  # Affichage d'un message d'erreur pour une mauvaise réponse
                    st.session_state.totanswer += 1  # Incrémentation du nombre total de réponses
                st.session_state['bouton'] = False  # Désactivation du bouton après avoir répondu
                st.experimental_rerun()  # Actualisation de la page

    with col22:
        if st.session_state['bouton']:
            if st.button("Fake"):  # Affichage du bouton "Fake"
                if label_val == 1:
                    st.write("su")  # Affichage d'un message de confirmation pour une bonne réponse
                    st.session_state.totanswer += 1  # Incrémentation du nombre total de réponses
                    st.session_state.goodanswer += 1  # Incrémentation du nombre de bonnes réponses
                else:
                    st.write("wrong")  # Affichage d'un message d'erreur pour une mauvaise réponse
                    st.session_state.totanswer += 1  # Incrémentation du nombre total de réponses
                st.session_state['bouton'] = False  # Désactivation du bouton après avoir répondu
                st.experimental_rerun()  # Actualisation de la page

with col1:
    st.header("The news :")  # Affichage du titre de la section
    if st.session_state.label:
        st.subheader(f'{data_false["items"][st.session_state.randint][1]}')  # Affichage de la question fausse
        st.write(f'{data_false["items"][st.session_state.randint][3]}')  # Affichage du contenu de la question fausse
    else:
        st.subheader(f'{data_true["items"][st.session_state.randint][1]}')  # Affichage de la question vraie
        st.write(f'{data_true["items"][st.session_state.randint][3]}')  # Affichage du contenu de la question vraie

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2015/12/01/15/43/black-1072366_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()  # Appel de la fonction pour ajouter l'arrière-plan à l'application
