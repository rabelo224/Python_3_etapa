import streamlit as st
import pandas as pd



st.write("Olá, mundo")




nome = "Davi"
idade = 18

st.write("Meu nome é", nome)
st.write("Minha idade é", idade)


st.divider()



st.title("Meu primeiro dash")
st.subheader(nome)



df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})



st.write(df)


st.divider()



st.subheader("Lista de supermercado")

produtos = {
    "Arroz": 17.00,
    "Feijão": 7.50,
    "Leite": 4.50,
    "Pão": 6.00,
    "Café": 18.00
}


produto = st.selectbox(
    "Selecione um produto:",
    list(produtos.keys())
)




quantidade = st.number_input(
    "Selecione a quantidade:",
    min_value=1,
    value=1
)




def calcular_preco(produto, quantidade):
    preco = produtos[produto]
    total = preco * quantidade
    return total



total = calcular_preco(produto, quantidade)



st.metric(
    "Preço total da compra",
    f"R$ {total:.2f}"
)