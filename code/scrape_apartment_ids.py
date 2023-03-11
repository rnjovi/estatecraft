import requests
from bs4 import BeautifulSoup

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=M1954069489'
    current_page = 1

    ids = []
    all_ids = set()

    while True:
        url = f"{base_url}?{query_string}&sivu={current_page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('div', {'class': 'ListPage__cardContainer__39dKQ'})

        for link in links:
            link2 = link.find('a', {'class': 'mui-style-58tli6 e12nd9f313'})
            id = link2.get('id')
            if id in all_ids:
                continue
            ids.append(id)
            all_ids.add(id)

        if len(links) / current_page == 30:
            current_page += 1
        else:
            break

    return ids