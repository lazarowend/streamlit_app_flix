import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewService
from movies.service import MovieService
from time import sleep


def show_reviews():
    review_service = ReviewService()
    movie_service = MovieService()

    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            key='reviews_grid',
            )
    else:
        st.warning('Não existe avaliações')

    st.title('Cadastrar nova Avaliação')
    movies = movie_service.get_movies()

    movie_options = {movie['title']: movie['id'] for movie in movies}

    selected_movie_title  = st.selectbox(
        'Selecione o Filme',
            options=(movie_options.keys())
    )

    stars = st.selectbox(
        'Estrelas',
        options=[1, 2, 3, 4, 5]
    )
    comment = st.text_area('Comentário')

    if st.button('Confirmar'):
        selected_movie_id = movie_options[selected_movie_title]
        review_service.create_review(
            movie=selected_movie_id,
            stars=stars,
            comment=comment,
        )
        st.success(f'Avaliação de {selected_movie_title} cadastrada com sucesso!')

        sleep(1)
        st.rerun()