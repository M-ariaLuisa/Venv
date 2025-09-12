import streamlit as st
import time

st.title("Média dos alunos")
st.header("Informe as notas do(a) aluno para calcular a média")

numero_1= st.number_input("Digite a 1º nota")
numero_2= st.number_input("Digite a 2º nota")
numero_3= st.number_input("Digite a 3º nota")
numero_4= st.number_input("Digite a 4º nota")

media= (numero_1 + numero_2 + numero_3 + numero_4) / 4

if st.button("Verificar"):
    st.write(f"A média do(a) aluno(a) é {media}")
else:
    st.info("Informe as notas")