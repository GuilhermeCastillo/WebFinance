import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

receitas = [
    {"descricao": "Bolo de chocolate", "valor": 1500, "data": "2024-03-15"},
    {"descricao": "Torta de morango", "valor": 2000, "data": "2024-03-16"},
    {"descricao": "Pudim de leite", "valor": 1800, "data": "2024-03-17"},
]


def show_receitas():
    st.write("Lista de Receitas")

    AgGrid(data=pd.DataFrame(receitas), reload_data=True, enableSorting=True, key="receitas_grid")

    descricao = st.text_input("Descricao")
    valor = st.text_input("Valor")
    data = st.text_input("Data")

    if st.button("Nova Receita"):
        st.success("Cadastro com sucesso!")
