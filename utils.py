import json

import constants
from models import Film

def load_film_object_from_json():
    with open(constants.FILMS_JSON_FILE) as json_file:
        data = json.load(json_file)
        if "films" not in data:
            data = {"films": data}
        films = []
        for film in data["films"]:
            films.append(Film(title=film["title"], dates=film['dates'], box_office_collections=film['box_office_collections']))
        
        return films
