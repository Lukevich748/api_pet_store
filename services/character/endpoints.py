
HOST = "https://rickandmortyapi.com/api"


class Endpoints:

    get_all_characters = f"{HOST}/character"
    get_character_by_id = lambda self, character_id: f"{HOST}/character/{character_id}"