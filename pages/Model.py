import streamlit as st  # Importation du module Streamlit pour créer l'application web
from Home import stemdata  # Importation des données
import random  # Importation du module random pour générer des nombres aléatoires
import requests  # Importation du module requests pour effectuer des requêtes HTTP
import pandas as pd  # Importation du module pandas pour manipuler les données sous forme de DataFrame

headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}

# Fonction pour obtenir la prédiction d'une nouvelle
def get_pred(text):
    return requests.get(f'https://appfake.azurewebsites.net/pred/?text={str(text)}')

# Fonction pour obtenir les résultats
def get_output():
    return requests.get(f"https://appfake.azurewebsites.net/dataoutput").json()

# Fonction pour générer une nouvelle question aléatoire
def new_rand():
    st.session_state['bouton'] = True
    st.session_state['label'] = random.getrandbits(1)
    st.session_state['randint'] = random.randint(0, 9)
    return

# Vérification et initialisation des variables d'état
if 'pred' not in st.session_state:
    st.session_state['pred'] = 0
if 'label' not in st.session_state:
    st.session_state['label'] = random.getrandbits(1)
if 'randint' not in st.session_state:
    st.session_state['randint'] = random.randint(0, 4)
if 'bouton' not in st.session_state:
    st.session_state['bouton'] = True

col01, col02, col03 = st.columns([6, 1, 2])  # Création de colonnes pour la mise en page
with col01:
    st.title(":red[Fake news] prediction")  # Affichage du titre de l'application
with col03:
    st.markdown("#")
    if st.button("Another news"):  # Affichage du bouton "Another news"
        new_rand()  # Appel de la fonction pour générer une nouvelle question aléatoire
        st.experimental_rerun()  # Actualisation de la page
    text = stemdata["items"][st.session_state.randint][3]  # Récupération du texte de la question

st.subheader(f'{stemdata["items"][st.session_state.randint][1]}')  # Affichage du titre de la question
st.write(f'{stemdata["items"][st.session_state.randint][3]}')  # Affichage du contenu de la question
st.write(f'{stemdata["items"][st.session_state.randint][2]}')  # Affichage de l'auteur de la question

col1, col2, col3 = st.columns([6, 1, 2])  # Création de nouvelles colonnes pour la mise en page
with col1:
    if st.button("predict"):  # Affichage du bouton "predict"
        st.session_state.pred = int(get_pred(text).json()[0])  # Obtention de la prédiction pour le texte de la question

        if st.session_state.pred == 1:
            st.markdown(
                f"![Alt Text](https://media.tenor.com/-Al8NY4CLRAAAAAC/donald-trump-fake-news.gif)")  # Affichage d'une animation pour une prédiction de fausse nouvelle
        if st.session_state.pred == 0:
            st.markdown(
                f"![Alt Text](https://media.tenor.com/wgkPy8pGP6UAAAAd/true-its-true.gif)")  # Affichage d'une animation pour une prédiction de vraie nouvelle

with col3:
    if st.button("send result"):  # Affichage du bouton "send result"
        requests.post(f'https://appfake.azurewebsites.net/addpred',
                      headers=headers, json={
                "id": stemdata["items"][st.session_state.randint][0],
                "title": stemdata["items"][st.session_state.randint][1],
                "author": stemdata["items"][st.session_state.randint][2],
                "text": stemdata["items"][st.session_state.randint][3],
                "pred": int(st.session_state.pred)
            })  # Envoi des résultats de prédiction à une URL

df = pd.DataFrame(columns=['id', "title", "author", "text", "label pred"])  # Création d'un DataFrame vide pour stocker les résultats
if st.button("load dataset"):  # Affichage du bouton "load dataset"
    data = get_output()  # Obtention des résultats
    df = df.head(0)
    for count, item in enumerate(data["items"]):
        new_row = pd.DataFrame({'id': item[0], 'title': item[1], \
                                'author': item[2], 'text': item[3], "label pred": item[4]}, index=[0])
        df = pd.concat([new_row, df]).reset_index(drop=True)  # Ajout des résultats au DataFrame
        df = df.sort_values("id")  # Tri des résultats par ID

if len(df.index) > 0:
    st.dataframe(df, use_container_width=True)  # Affichage des résultats sous forme de tableau

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2021/06/27/09/21/fish-6368233_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()  # Appel de la fonction pour ajouter l'arrière-plan à l'application
