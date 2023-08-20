import requests
from bs4 import BeautifulSoup

search_id = 'M1999388199'

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=' + search_id
    current_page = 1

    ids = []
    all_ids = set()

    with requests.Session() as session:
        while True:
            url = f"{base_url}?{query_string}&sivu={current_page}"
            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', {'class': 'mui-style-1w82bvv e10l6nir1'})

            new_ids = []
            for link in links:
                id = link.get('id')
                if id in all_ids:
                    continue
                new_ids.append(id)
                all_ids.add(id)

            if len(new_ids) > 0:
                ids.extend(new_ids)
                current_page += 1
            else:
                break

            if len(new_ids) < 30:
                break

    return ids