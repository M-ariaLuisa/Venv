import streamlit as st

st.title("Boletim")
st.header("Informe as notas para descobrir a média do aluno(a) e se ele(a) foi aprovado, reprovado ou vai para a recupereção ")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    nota = st.number_input(f"Digite a {i+1}ª nota:")
    soma = soma + nota


media = soma / QUANTIDADE_NOTAS

if st.button("Verificar"):
    st.info(f"Média:{media}")
    if media >= 7:
        st.success(" Aprovado(a)") 
    elif media >= 4:   
        st.error("Recuperação")     
    else:
        st.info("Reprovado(a)")
     