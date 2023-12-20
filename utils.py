import requests 
from bs4 import BeautifulSoup

from models import Film, FilmRecord

from llm import query_gpt4_non_function

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

    query = """
    Your role is to generate a simplified document which contains the following information comma separated:
    {title of the film}, {list of unique months for that title}, {cumulative box_office_collection}
    minimise the tokens used in the response
    """
    films = list(films_dict.values())
    # split films into 2
    films_1, films_2 = films[:len(films)//2], films[len(films)//2:]

    data1 = query_gpt4_non_function(query, 400, "gpt-3.5-turbo", str([film.dict() for film in films_1]))
    data2 = query_gpt4_non_function(query, 400, "gpt-3.5-turbo", str([film.dict() for film in films_2]))
    data = data1 + data2    
    print(data)

    return data

