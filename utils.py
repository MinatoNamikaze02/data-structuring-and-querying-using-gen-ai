import os
import json
import requests 
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import constants
from models import Film

from llm import query_longshot, query_gpt4_non_function

load_dotenv()

def load_film_object_from_json():
    with open(constants.FILMS_JSON_FILE) as json_file:
        data = json.load(json_file)
        if "films" not in data:
            data = {"films": data}
        films = []
        for film in data["films"]:
            films.append(Film(title=film["title"], dates=film['dates'], box_office_collections=film['box_office_collections']))
        
        return films

def fetch_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable sortable'})

    query = f"""
    Please convert this given unstructured table tag into a summarised formatted text with the following comma separated fields:
    [title], [dates], [box_office_collections]
    Do not return html tags or links in the response.
    {str(table)}
    """
    # films = list(films_dict.values())
    # rows_1, rows_2, rows_3 = str(rows_1), str(rows_2), str(rows_3)
    data = query_longshot(query, 10000, constants.MISTRAL_7B_INSTRUCT_V0_2)
    # data2 = query_gpt4_non_function(query, 200, "gpt-3.5-turbo", rows_2)
    # data3 = query_gpt4_non_function(query, 200, "gpt-3.5-turbo", rows_3)
    print(data)
    query1 = f"""
    convert the given data to a JSON object with the following fields:
    1. title: Title of the film
    2. dates: List of dates for that film (in %Y-%m-%d format)
    3. box_office_collections: List of box office collections for that film
    Ignore any links or html tags in the response.
    """
    formatted_json = query_gpt4_non_function(query1, 2048, constants.GPT_3_5_TURBO, data)
    print("gpt", formatted_json)
    return formatted_json

if __name__ == "__main__":
    data = json.loads(fetch_html(os.getenv("url")))
    films = []
    if "films" not in data:
        data = {"films": data}
    for film in data["films"]:
        print(film)
        films.append(Film(title=film["title"], dates=film['dates'], box_office_collections=film['box_office_collections']))

    print(films)
    # dump object to file
    with open(constants.FILMS_JSON_FILE, 'w') as outfile:
        json.dump(data, outfile)
