import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

reviews = [
    {'ID': 1, 'movie': 'Teste', 'stars': '5', 'comment': 'lorem ipsum'},
]


def show_reviews():
    st.write('Lista de Avaliações')

    AgGrid(
        data=pd.DataFrame(reviews),
        key='reviews_grid',
        )

    st.title('Cadastrar nova Avaliação')
    movie = st.text_input('Nome do Gênero')
    stars = st.number_input('Estrelas', min_value=1, max_value=5, step=1)
    comment = st.text_area('Comentário')
    if st.button('Confirmar'):
        st.success(f'Avaliação de {movie} cadastrado com sucesso!')