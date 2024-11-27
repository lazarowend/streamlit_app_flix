import streamlit as st 
import requests
from login.service import logout


class MovieRepository:


    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__movie_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movie_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movie_url,
            data=movie,
            headers=self.__headers
        )

        if response.status_code == 201:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao criar um Filme. Status code: {response.status_code}')

    def update_movie(self, movie):
        movie_update_url = f'{self.__movie_url}{movie["id"]}/'
        response = requests.put(
            movie_update_url,
            data=movie,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao atualizar um Filme. Status code: {response.status_code}')

    def delete_movie(self, movie_id):
        movie_delete_url = f'{self.__movie_url}{movie_id}/'
        response = requests.delete(
            movie_delete_url,
            headers=self.__headers
        )

        if response.status_code == 204:
            return {"message": "Filme deletado com sucesso"}
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao deletar um Filme. Status code: {response.status_code}')

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movie_url}stats/',
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code {response.status_code}')