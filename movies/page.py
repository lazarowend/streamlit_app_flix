import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

movies = [
    {'ID': 1, 'Genero': 'Teste', 'Data de Lançameto': '5', 'atores': {
        '1': 'atore1',
        '2': 'atore2',
    }},
]


def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        key='movies_grid',
        )

    st.title('Cadastrar novo Filme')
    movie = st.text_input('Nome do Gênero')
    stars = st.number_input('Estrelas', min_value=1, max_value=5, step=1)
    comment = st.text_area('Comentário')
    if st.button('Confirmar'):
        st.success(f'Avaliação de {movie} cadastrado com sucesso!')