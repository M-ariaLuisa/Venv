import streamlit as st
import time

st.title("Atividade")
st.header("Laço de repetição- For")

st.write("")

soma = 0

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}° número: " , step=1, min_value=0)
    soma =soma + numero
    time.sleep(1)

if st.button("Iniciar"):
    st.sucess(f"A soma dos números é: {soma}")
else:
    st.info("Informe um número")