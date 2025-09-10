import streamlit as st
import time

st.title("Laço de repetição - FOR")

st.header("Contagem de 1 a 10")

numero= st.number_input("Digite até onde quer o laço de repetição", step=1)


if st.button("Iniciar"):
    for i in range(1,11):
        st.write(i)
        time.sleep(1)
    
    st.header("fim")
