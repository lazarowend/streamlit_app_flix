import streamlit as st 
import requests
from login.service import logout

class ActorRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__actor_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actor_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actor_url,
            data=actor,
            headers=self.__headers
        )

        if response.status_code == 201:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao criar um ator/atriz. Status code: {response.status_code}')

    def update_actor(self, actor):
        actor_update_url = f'{self.__actor_url}{actor["id"]}/'
        response = requests.put(
            actor_update_url,
            data=actor,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao atualizar um ator/atriz. Status code: {response.status_code}')

    def delete_actor(self, actor_id):
        actor_delete_url = f'{self.__actor_url}{actor_id}/'
        response = requests.delete(
            actor_delete_url,
            headers=self.__headers
        )

        if response.status_code == 204:
            return {"message": "ator/atriz deletado com sucesso"}
        
        if response.status_code == 401:
            logout()
            return None
        
        raise Exception(f'Erro ao deletar um ator/atriz. Status code: {response.status_code}')
