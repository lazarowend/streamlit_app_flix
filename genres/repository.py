import streamlit as st 
import requests
from login.service import logout

class GenreRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__genre_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genre_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_genre(self, genre):
        response = requests.post(
            self.__genre_url,
            data=genre,
            headers=self.__headers
        )

        if response.status_code == 201:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao criar um gênero. Status code: {response.status_code}')

    def update_genre(self, genre):
        genre_update_url = f'{self.__genre_url}{genre["id"]}/'
        response = requests.put(
            genre_update_url,
            data=genre,
            headers=self.__headers
        )

        if response.status_code == 200:  # Código 200 para sucesso em update
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao atualizar um gênero. Status code: {response.status_code}')

    def delete_genre(self, genre_id):
        genre_delete_url = f'{self.__genre_url}{genre_id}/'
        response = requests.delete(
            genre_delete_url,
            headers=self.__headers
        )

        if response.status_code == 204:  # Código 204 para sucesso em delete
            return {"message": "Gênero deletado com sucesso"}
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao deletar um gênero. Status code: {response.status_code}')
