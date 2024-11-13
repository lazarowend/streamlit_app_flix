import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
from time import sleep


NATIONALITY_CHOICES = (
    ('US', 'Estados Unidos'),
    ('GB', 'Reino Unido'),
    ('FR', 'França'),
    ('IT', 'Itália'),
    ('AU', 'Austrália'),
    ('CA', 'Canadá'),
    ('DE', 'Alemanha'),
    ('JP', 'Japão'),
    ('IN', 'Índia'),
    ('BR', 'Brasil'),
)


def get_abbreviation_by_country(country_name):
    for abbreviation, country in NATIONALITY_CHOICES:
        if country == country_name:
            return abbreviation
    return None


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')

        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key='actors_grid',
            )
    else:
        st.warning('Não exite Atores/Atrizes')

    st.title('Cadastrar novo Ator/Atriz')

    name = st.text_input('Nome do Gênero')
    birthday = st.date_input('Data de Nascimento')
    nationality = st.selectbox('Selecione a Nacionalidade', options=[x[1] for x in NATIONALITY_CHOICES])
    abbreviation = get_abbreviation_by_country(nationality)

    if st.button('Confirmar'):
        if len(name) == 0:
            st.warning('Nome inválido')
        elif birthday is None:
            st.warning('Aniversário inválido')
        elif abbreviation is None:
            st.warning('Nacionalidade inválida')
        else:
            actor_service.create_actor(name, birthday, abbreviation)
            st.success(f'Ator/Atriz {name} cadastrado(a) com sucesso!')
            sleep(1)
            st.rerun()
