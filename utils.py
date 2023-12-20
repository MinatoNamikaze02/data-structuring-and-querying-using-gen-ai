import requests 
from bs4 import BeautifulSoup

from models import Film, FilmRecord

def fetch_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable sortable'})

    rows = table.find_all('tr')

    films_dict = {}
    skip = 0
    current_title = None
    for row in rows[1:]:
        cells = row.find_all('td')

        if skip > 0:
            skip -= 1
            date = cells[1].text.strip()
            gross = int(''.join(cells[2].text.strip().split('$')[1].split(',')))
            notes = cells[3].text.strip()
        else:
            current_title = cells[2].text.strip()
            skip = int(cells[2].get('rowspan', 0)) - 1
            
            date = cells[1].text.strip()
            gross = int(''.join(cells[3].text.strip().split('$')[1].split(',')))
            notes = cells[4].text.strip()

        record = FilmRecord(date=date, box_office_collection=gross, notes=notes)

        if current_title in films_dict:
            films_dict[current_title].records.append(record)
        else:
            films_dict[current_title] = Film(title=current_title, records=[record])

    films = list(films_dict.values())
    return films

# if __name__ == '__main__':
#     films = fetch_html('https://en.wikipedia.org/wiki/List_of_2023_box_office_number-one_films_in_the_United_States')
#     json_data = [film.model_dump() for film in films]
#     import json
#     print(json_data)
#     with open('films.json', 'w') as f:
#         json.dump(json_data, f)
