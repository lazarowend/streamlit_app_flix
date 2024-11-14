import streamlit as st 
import requests
from login.service import logout


class ReviewRepository:


    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__review_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            self.__review_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_review(self, review):
        response = requests.post(
            self.__review_url,
            data=review,
            headers=self.__headers
        )

        if response.status_code == 201:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao criar um Filme. Status code: {response.status_code}')

    def update_review(self, review):
        review_update_url = f'{self.__review_url}{review["id"]}/'
        response = requests.put(
            review_update_url,
            data=review,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao atualizar uma Avaliação. Status code: {response.status_code}')

    def delete_review(self, review_id):
        review_delete_url = f'{self.__review_url}{review_id}/'
        response = requests.delete(
            review_delete_url,
            headers=self.__headers
        )

        if response.status_code == 204:
            return {"message": "Filme deletado com sucesso"}
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao deletar uma Avaliação. Status code: {response.status_code}')
