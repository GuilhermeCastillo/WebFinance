import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

despesas = [
    {
        "descricao": "Bolo de chocolate",
        "valor": 1500,
        "data": "2024-03-15",
        "categoria": 4,
    },
    {
        "descricao": "Torta de morango",
        "valor": 2000,
        "data": "2024-03-16",
        "categoria": 3,
    },
    {
        "descricao": "Pudim de leite",
        "valor": 1800,
        "data": "2024-03-17",
        "categoria": 1,
    },
]


def show_despesas():
    st.write("Lista de Receitas")

    AgGrid(
        data=pd.DataFrame(despesas),
        reload_data=True,
        enableSorting=True,
        key="despesas_grid",
    )

    descricao = st.text_input("Descricao")
    valor = st.text_input("Valor")
    data = st.text_input("Data")
    categoria = st.text_input("Categoria")

    if st.button("Nova Receita"):
        st.success("Cadastro com sucesso!")
