#Escrever um algoritmo que mostra os
#números pares entre 100 e 120.

import streamlit as st
import time

st.title("Atividade 2")

st.header("Laço de repetição: FOR")

st.header("Escrever um algoritmo que mostra os números pares entre 1 e 20")
st.write("Clique no botão para iniciar")

if st.button("Iniciar "):
    for i in range(1,20,2):
        st.info(i)
        time.sleep(2)  

st.header("Fim")