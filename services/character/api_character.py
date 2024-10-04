from typing import Optional

import  allure
import requests
from utils.helper import Helper
from services.character.payloads import Payloads
from services.character.endpoints import Endpoints
from services.character.models.model_all_characters import AllCharactersModel
from services.character.models.model_one_character import OneCharacterModel


class CharacterAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()

    @allure.step("Get all characters")
    def get_all_characters(self, expected_result=True) -> Optional[AllCharactersModel]:
        response = requests.get(
            url=self._endpoints.get_all_characters,
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = AllCharactersModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()
            return None

    @allure.step("Get Character By ID")
    def get_character_by_id(self, character_id, expected_result=True) -> Optional[OneCharacterModel]:
        response = requests.get(
            url=self._endpoints.get_character_by_id(character_id),
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = OneCharacterModel(**response.json())
            assert int(character_id) == model.id, response.json()
            return model
        else:
            assert response.status_code != 200, response.json()
            return None
