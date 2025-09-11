import streamlit as st
import time

st.title("Atividade")
st.header("Soma")
st.write("")

numero_1 =  st.number_input("Digite o primeiro número inteiro: ", step=1, min_value=0)
numero_2 =  st.number_input("Digite o segundo número inteiro: ", step=1, min_value=0)
numero_3= st.number_input("Digite o terceiro número inteiro :", step=1, min_value=0)
numero_4= st.number_input("Digite o quarto número inteiro: ", step=1,min_value=0)
numero_5=st.number_input("Digite o quinto número inteiro: ", step=1,min_value=0)
soma= numero_1 + numero_2+ numero_3 + numero_4 + numero_5

if st.button("Iniciar"):
    st.info(f"{numero_1} + {numero_2} + {numero_3} + {numero_4} + {numero_5}")
    st.info(f"O resultado é {soma}")


