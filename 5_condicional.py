# Verificando a média
# Solicite ao usuário a média do aluno
# Se maior ou igual a 7, mostre como aprovado
# Caso contrário, mostre como reprovado.

import streamlit as st

st.title("Boletim")

media = st.number_input("Digite a média do aluno: ")

if st.button("Verificar"):
    if media >= 7:
        st.success("Aprovado!")
    else:
        st.error("Reprovado!")

else:
    st.info("Informe a média.")
    
 # sucess- verde
 # warning- amarelo
 # info- azul
 # error- vermelho
