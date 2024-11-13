import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

genres = [
{'id': 1, 'name': 'teste'}
]

def show_genres():
    st.write('Lista de Gêneros')

    AgGrid(
        data=pd.DataFrame(genres)
        )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Confirmar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')