# Escreva um algoritmo que solicite do usuário um número
# e mostre a tabuada de multiplicação do número informado

import streamlit as st
import time

st.title("Atividade 3")
st.header("Tabuada")

numero=st.number_input("Digite um número")



if st.button("Iniciar"):
    for i in range(1,10,1):
        st.write(f"{numero} *{range}")