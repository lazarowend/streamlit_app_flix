import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

genres = [
    {'ID': 1, 'Gênero': 'Teste'},
    {'ID': 2, 'Gênero': 'Aventura'},
]


def show_genres():
    st.write('Lista de Gêneros')

    AgGrid(
        data=pd.DataFrame(genres),
        key='genre_grid'
        )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Confirmar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')