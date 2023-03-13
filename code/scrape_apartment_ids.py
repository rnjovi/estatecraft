import lxml
import cchardet
import requests
from bs4 import BeautifulSoup

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=M1954069489'
    current_page_num = 1

    unique_ids = set()
    all_ids = []

    # get the number of pages from the first page of the search results
    first_page_url = f"{base_url}?{query_string}&sivu=1"
    response = requests.get(first_page_url)
    soup = BeautifulSoup(response.content, 'lxml')
   
    elements = soup.find_all('button', {'class': 'theme__button__1YqFK theme__flat__13aFK theme__button__1YqFK theme__squared__17Uvn theme__neutral__1F1Jf Button__button__3K-jn Pagination__button__3H2wX'})
    last_element = elements[-1]
    value = int(last_element.text.strip())

    # loop through all pages
    while current_page_num <= value:
        current_page_url = f"{base_url}?{query_string}&sivu={current_page_num}"
        response = requests.get(current_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        apartment_links = soup.find_all('div', {'class': 'ListPage__cardContainer__39dKQ'})

        for link in apartment_links:
            apartment_link = link.find('a', {'class': 'mui-style-58tli6 e12nd9f313'})
            apartment_id = apartment_link.get('id')
            if apartment_id in all_ids:
                continue
            all_ids.append(apartment_id)
            unique_ids.add(apartment_id)

        current_page_num += 1

    return all_ids