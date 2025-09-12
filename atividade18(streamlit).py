import streamlit as st

st.title("Laço de repetição - For")

nota_1= st.number_input("Digite a 1ª nota : ", step=1)
nota_2= st.number_input("Digite a 2ª nota : ", step=1)

quantidade_notas = 2
soma = 0
for i in range:
    while True: 
    if 0 <= nota_1 <= 10 and 0 < nota_2 <= 10:
        st.warning("A nota deve ser entre 0 e 10.")
        media =  (nota_1 + nota_2) / 2
        st.write("Média: {media}")
else:
      st.warning("A nota deve ser entre 0 e 10.")
