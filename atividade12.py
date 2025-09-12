#Escreva um algoritmo que solicite ao usuário 5 valores inteiros 
#e ao final mostre a quantidade de numeros impares e pares

import streamlit as st
import time

pares = 0
impares = 0

st.title("Verificando pares e impares")

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}° número:", step=1)
    if numero % 2 == 0:
      pares = pares + 1
    else:
     impares = impares + 1

if st.button("Verificar"):
    st.info(f"Quantidade de pares :{pares} ")
    st.info(f"Quantidade de impares :{impares}")       

