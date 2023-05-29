import streamlit as st
import requests
import random
from streamlit_app import data_false,data,data_true


if 'label' not in st.session_state:
    st.session_state['label'] = random.getrandbits(1)
if 'randint' not in st.session_state:
    st.session_state['randint'] = random.randint(0,9)
if 'bouton' not in st.session_state:
    st.session_state['bouton'] = True
# if 'goodanswer' not in st.session_state:
#     st.session_state["Goodanswer"] = st.session_state.get("Goodanswer", 20)

def new_rand() :
    st.session_state['bouton'] = True
    st.session_state['label'] = random.getrandbits(1)
    st.session_state['randint'] = random.randint(0,9)
    return


col01,col02,col03 = st.columns([6,1,4])
with col01 :
    st.title(":red[Fake news] or not ?")
with col03 :
    if st.button("Another news") :
        new_rand()
        st.experimental_rerun()


col1,col2,col3 = st.columns([6,1,4])
with col3:
    bar = st.progress(st.session_state["Goodanswer"],"Good answer" )
    st.header("What do you :red[think] ?")

    if st.session_state.label == 0 :
        label_val = data_true["items"][st.session_state.randint][4]
    else :
        label_val = data_false["items"][st.session_state.randint][4]

    col11,col22 = st.columns(2)

    with col11 :
        if st.session_state['bouton'] :
            if st.button("Not Fake"):
                if label_val == 0 :
                    st.write("su")
                    # st.session_state["Goodanswer"] = st.session_state["Goodanswer"] + 20
                else :
                    st.write("wrong")

                st.session_state['bouton'] = False
    with  col22 :
        if st.session_state['bouton'] :
            if st.button("Fake"):
                if label_val == 1 :
                    st.write("su")
                    # st.session_state["Goodanswer"] = st.session_state["Goodanswer"] + 20
                else :
                    st.write("wrong")

            st.session_state['bouton'] = False
with col1 :
    st.header("The news :")
    if  st.session_state.label :
        st.subheader(f'{data_false["items"][st.session_state.randint][1]}')
        st.write(f'{data_false["items"][st.session_state.randint][3]}')
    else :
        st.subheader(f'{data_true["items"][st.session_state.randint][1]}')
        st.write(f'{data_true["items"][st.session_state.randint][3]}')
