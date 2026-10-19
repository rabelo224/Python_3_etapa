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

# 9 - Calculadora de troco

st.divider()
st.subheader("Calculadora de Troco")

col1, col2 = st.columns(2)

with col1:
    valor_compra = st.number_input(
        "Valor da compra:",
        value=float(total),
        step=1.0
    )

with col2:
    dinheiro_pago = st.number_input(
        "Dinheiro pago:",
        value=0.0,
        step=1.0
    )

# Botão para calcular o troco
if st.button("Calcular Troco", type="primary"):
    if dinheiro_pago < valor_compra:
        st.error("O valor pago é menor que o valor da compra.")
    else:
        resultado = dinheiro_pago - valor_compra
        st.success(f"**Troco:** R$ {resultado:.2f}")