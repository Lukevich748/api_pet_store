from services.character.api_character import CharacterAPI


class BaseTest:

    def setup_method(self):
        self.api_character = CharacterAPI()