import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

actors = [
    {'ID': 1, 'name': 'Teste', 'data de nacimento': '1111-11-11', 'Nacionalidade': 'BR'},
    {'ID': 2, 'name': 'Teste', 'data de nacimento': '1111-11-11', 'Nacionalidade': 'BR'},
    {'ID': 3, 'name': 'Teste', 'data de nacimento': '1111-11-11', 'Nacionalidade': 'BR'},
]


def show_actors():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data=pd.DataFrame(actors),
        key='actors_grid',
        )

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Gênero')
    birthday = st.date_input('Data de Nascimento')
    nationality = st.text_input('Nacionalidade')
    if st.button('Confirmar'):
        st.success(f'Ator/Atriz {name} cadastrado(a) com sucesso!')