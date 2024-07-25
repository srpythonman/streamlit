import streamlit as st
import pandas as pd
from datetime import date

data_min = date(1900, 1, 1)
data_max = date(2100, 12, 31)

def gravar_dados(nome, dt_nasc, natureza_juridica):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {natureza_juridica}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

def reiniciar_formulario():
    st.session_state["nome"] = ""
    st.session_state["dt_nasc"] = date(2024, 7, 24)
    st.session_state["natureza_juridica"] = ""

st.set_page_config(page_title="Cadastro de clientes", 
                   page_icon="📝" 
)

st.title("Cadastro de cliente")
st.divider()

nome = st.text_input("Digite seu nome completo", 
                     key="nome_cliente"
).upper()

dt_nasc = st.date_input("Digite sua data de nascimento", 
                        value=date(2024, 7, 24), 
                        min_value=data_min, 
                        max_value=data_max, 
                        format="DD/MM/YYYY"
)
natureza_juridica = st.selectbox("Tipo de cliente", 
                                 ["Pessoa física", "Pessoa jurídica"]
)

col1, col2 = st.columns(2)
with col1:
    btn_cadastrar = st.button("Cadastrar")
with col2:
    btn_reiniciar = st.button("Reiniciar")

if btn_cadastrar:
    gravar_dados(nome, dt_nasc, natureza_juridica)
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Erro ao cadastrar cliente!", icon="❌")

if btn_reiniciar:
    reiniciar_formulario()