
import allure
import pytest
from allure_commons.types import Severity
from config.base_test import BaseTest


@allure.epic("Character Management")
class TestCharacter(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.feature("Character Info")
    @allure.story("Get All Characters")
    def test_get_all_characters(self):
        self.api_character.get_all_characters()




    @pytest.mark.smokes
    @allure.severity(Severity.NORMAL)
    @allure.feature("Character info")
    @allure.story("Get One Character By ID")
    @pytest.mark.parametrize(
        "character_id, expected_result", [
            (2, True),
            (10, True),
            ("14", True),
            (0, False),
            (-1, False),
            (None, False),
        ]
    )
    def test_get_character_by_id(self, character_id, expected_result):
        self.api_character.get_character_by_id(character_id, expected_result)