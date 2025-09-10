import streamlit as st

st.title("Atividade")

numero_1= st.number_input("Digite o primeiro numero")
numero_2= st.number_input("Digite o segundo numero")

media= (numero_1 + numero_2 )/ 2
soma= numero_1 + numero_2
produto= numero_1 * numero_2
menor= min(numero_1, numero_2)
maior_valor=max(numero_1,numero_2)

if st.button("Verificar"):
    if numero_1 and numero_2:
        st.write(f"Soma:{soma}")
        st.write(f"Média:{media}")
        st.write(f"Produto:{produto}")
        st.write(f"Maior valor: {maior_valor}")
        st.write(f"Menor Valor:{menor}")

else:
    st.info("Informe os números")



