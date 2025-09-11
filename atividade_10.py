#Escrever um algoritmo que solicite ao usuário um número 
# e faça a contagem regressiva a partir do número informado até o numero 1

import streamlit as st
import time

st.header("Laço de repetição- FOR")
st.header("Contagem regressiva")
st.write("Escrever um algoritmo que solicite ao usuário um número e faça a contagem regressiva a partir do número informado até o numero 1")

numero =  st.number_input("Digite um número: ", step=1, min_value=0)

if st.button("Iniciar"):
    for i in range (numero, 0, -1):
        st.warning(i)
        time.sleep(1) 
    st.header("Fim")
else:
    st.info("Informe um número")