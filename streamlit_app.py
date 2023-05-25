import streamlit as st
import requests
import random
from streamlit_extras.let_it_rain import rain


@st.cache_data
def get_data(label,lengthtext,nbrow):
    return requests.get(f"https://appfake.azurewebsites.net/5data/\
?label={label}&lengthtext={lengthtext}&nbrow={nbrow}").json()
def get_rand() :
    random_label = random.getrandbits(1)
    randint = random.randint(0,9)
    return random_label,randint
data_true = get_data(0,300,10)
data_false = get_data(1,300,10)
random_label,randint = get_rand()


st.title("Fake ou pas ?")





if  random_label :
    st.subheader(f'{data_false["items"][randint][1]}')
    st.write(f'{data_false["items"][randint][3]}')
else :
    st.subheader(f'{data_true["items"][randint][1]}')
    st.write(f'{data_true["items"][randint][3]}')
col1,col2 = st.columns(2)
with col1 :
    if st.button("Not Fake"):

        if data_true["items"][randint][4] == 0 :
            rain(emoji="👌",font_size=54,falling_speed=2,animation_length="infinite")
        else :
            rain(emoji="⛔",font_size=54,falling_speed=2,animation_length="infinite")
        random_label,randint = get_rand()

with col2 :
    if st.button("Fake"):
        if data_true["items"][randint][4] == 1 :
            rain(emoji="👌",font_size=54,falling_speed=3,animation_length="infinite")
        else :
            rain(emoji="⛔",font_size=54,falling_speed=3,animation_length="infinite")
        random_label,randint = get_rand()
