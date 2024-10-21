from idlelib.configdialog import is_int

import allure
import pytest
from allure_commons.types import Severity
from config.base_test import BaseTest
from faker import Faker
fake = Faker()


@allure.epic("Character Management")
class TestCharacter(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.feature("Character Info")
    @allure.story("Get All Characters")
    @pytest.mark.parametrize(
        "params, expected_result", [
            # Positive cases
            ({"name": "Campaign Manager Morty", "status": "Dead", "species": "Human", "type": "", "gender": "Male"}, True),
            ({"name": "Rick Sanchez", "status": "Alive", "species": "Human", "type": "", "gender": "Male"}, True),
            ({"name": "Woman Ric", "status": "Alive", "species": "Alien", "type": "Chair", "gender": "Female"}, True),
            ({"status": "Alive", "species": "Human"}, True),
            ({"gender": "Male"}, True),
            ({"gender": "Female"}, True),

            # Negative cases
            ({"name": f"{fake.name_male()}", "status": f"{fake.state()}", "species": "Alien", "type": "Chair", "gender": "Female"}, False),
            ({"name": f"{fake.name_male()}", "status": f"{fake.state()}", "species": "Human", "type": "", "gender": "Male"}, False),
            ({"name": f"{fake.name_male()}", "status": f"{fake.state()}", "species": "Alien", "type": "Chair", "gender": "Female"}, False),
        ]
    )
    def test_get_all_characters(self, params, expected_result):
        self.api_character.get_all_characters(params, expected_result)

    @pytest.mark.smokes
    @allure.severity(Severity.NORMAL)
    @allure.feature("Character info")
    @allure.story("Get One Character By ID")
    @pytest.mark.parametrize(
        "character_id, expected_result", [
            # Positive cases
            (1, True),
            (2, True),
            (10, True),
            (40, True),

            # Negative cases
            ("'14'", False),
            ("one", False),
            (0, False),
            (-1, False),
            (None, False),
        ]
    )
    def test_get_character_by_id(self, character_id, expected_result):
        self.api_character.get_character_by_id(character_id, expected_result)

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.feature("Character info")
    @allure.story("Get Multiple Character By ID")
    @pytest.mark.parametrize(
        "character_ids, expected_result", [
            # Positive cases
            ([1, 10, 13], True),
            ([3, 6], True),

            # Negative cases
            ([], False),
            (None, False)
        ]
    )
    def test_get_multiple_characters(self, character_ids: list[int], expected_result: bool):
        self.api_character.get_multiple_characters(character_ids, expected_result)