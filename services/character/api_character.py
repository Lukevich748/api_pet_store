from typing import Optional
import  allure
import requests
from utils.helper import Helper
from services.character.payloads import Payloads
from services.character.endpoints import Endpoints
from services.character.models.model_all_characters import AllCharactersModel
from services.character.models.model_one_character import OneCharacterModel
from services.character.models.model_multiple_characters import MultipleCharactersModel


class CharacterAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()

    @allure.step("Get all characters")
    def get_all_characters(self, params, expected_result=True):
        response = requests.get(
            url=self._endpoints.get_all_characters,
            params=params
        )
        return self.validate_response(response=response, model=AllCharactersModel, status_code=200, expected_result=expected_result)


    @allure.step("Get Character By ID")
    def get_character_by_id(self, character_id: int, expected_result=True) -> Optional[OneCharacterModel]:
        response = requests.get(
            url=self._endpoints.get_character_by_id(character_id),
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = OneCharacterModel(**response.json())
            assert character_id == model.id, response.json()
            return model
        else:
            assert response.status_code != 200, response.json()
            return None

    @allure.step("Get Multiple Character By IDs")
    def get_multiple_characters(self, character_ids: list[int], expected_result=True) -> Optional[list[MultipleCharactersModel]]:
        response = requests.get(
            url=self._endpoints.get_multiple_characters(character_ids)
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = ([MultipleCharactersModel(**item) for item in response.json()])
            assert character_ids == [character.id for character in model], response.json()
            return model
        else:
            assert response.status_code != 200, response.json()
            return None
