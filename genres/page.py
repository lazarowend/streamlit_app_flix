import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService
import time

def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')
        genres_df = pd.json_normalize(genres)

        AgGrid(
            data=genres_df,
            key='genre_grid'
            )
    else:
        st.warning('Nenhum Gênero cadastrado')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Confirmar'):
        if len(name) == 0:
            st.warning("Gênero Inválido")
        else:
            genre_service.create_genre(name)
            st.success(f'Gênero {name} cadastrado com sucesso!')
            time.sleep(1)
            st.rerun()