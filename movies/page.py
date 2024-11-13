import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService
from time import sleep


def show_movies():
    movie_service = MovieService()
    actor_service = ActorService()
    genre_service = GenreService()

    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')

        movies_df = pd.json_normalize(movies)
        AgGrid(
            data=movies_df,
            key='movies_grid',
            )
    else:
        st.warning('Não existe filmes cadastrados')


    actors = actor_service.get_actors()
    genres = genre_service.get_genres()

    st.title('Cadastrar novo Filme')
    title = st.text_input('Título')

    genre_options = {genre['name']: genre['id'] for genre in genres}
    selected_genres = st.multiselect(
        label='Selecione os Gêneros',
        options=list(genre_options.keys()),
        placeholder='Selecione os Gêneros'
    )

    actor_options = {actor['name']: actor['id'] for actor in actors}
    selected_actors = st.multiselect(
        label='Selecione os Atores/Atrizes',
        options=list(actor_options.keys()),
        placeholder='Selecione os Atores/Atrizes'
    )

    release_date = st.date_input('Data de Lançamento')
    resume = st.text_input('Resumo')

    if st.button('Confirmar'):
        selected_genre_ids = [genre_options[genre] for genre in selected_genres]
        selected_actor_ids = [actor_options[actor] for actor in selected_actors]

        movie_service.create_movie(title, selected_genre_ids, release_date, selected_actor_ids, resume)
        st.success(f'Filme {title} foi cadastrado com sucesso!')

        sleep(1)
        st.rerun()