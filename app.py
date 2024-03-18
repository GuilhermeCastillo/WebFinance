import streamlit as st
from receitas.page import show_receitas
from despesas.page import show_despesas
from login.page import show_login


def main():

    if "token" not in st.session_state:
        show_login()

    else:
        st.title("WebFinance")

        menu_option = st.sidebar.selectbox(
            "Selecione uma opcao: ", ["Inicio", "Receitas", "Despesas", "Resumo"]
        )

        if menu_option == "Inicio":
            st.write("Inicio")

        if menu_option == "Receitas":
            show_receitas()

        if menu_option == "Despesas":
            show_despesas()

        if menu_option == "Resumo":
            st.write("Resumo")


if __name__ == "__main__":
    main()
