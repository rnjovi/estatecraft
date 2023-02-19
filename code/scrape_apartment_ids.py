import requests
from bs4 import BeautifulSoup

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=M1946406847'
    current_page = 1

    ids = []
    all_ids = set()

    while True:
        url = f"{base_url}?{query_string}&sivu={current_page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', {'class': 'AnnouncementCard__CardLink-sc-xmfue4-1 dnspFg'})

        for link in links:
            id = link['id']
            if id in all_ids:
                continue
            ids.append(id)
            all_ids.add(id)

        if len(links) / current_page == 30:
            current_page += 1
        else:
            break

    return ids