
import requests
from bs4 import BeautifulSoup

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=M1954707357'
    current_page_num = 1

    unique_ids = set()
    all_ids = []

    # Create a session object for reusing the underlying TCP connection
    session = requests.Session()

    # get the number of pages from the first page of the search results
    first_page_url = f"{base_url}?{query_string}&sivu=1"
    response = session.get(first_page_url)
    soup = BeautifulSoup(response.content, 'lxml')
   
    elements = soup.find_all('button', {'class': 'theme__button__1YqFK theme__flat__13aFK theme__button__1YqFK theme__squared__17Uvn theme__neutral__1F1Jf Button__button__3K-jn Pagination__button__3H2wX'})

    last_element = elements[-1] if elements else None
    value = int(last_element.text.strip()) if last_element else 1

    # loop through all pages
    for current_page_num in range(1, value+1):
        current_page_url = f"{base_url}?{query_string}&sivu={current_page_num}"
        response = session.get(current_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        apartment_links = soup.find_all('div', {'class': 'ListPage__cardContainer__39dKQ'})

        # Use list comprehension to extract apartment ids
        new_ids = [link.find('a', {'class': 'mui-style-58tli6 e12nd9f313'}).get('id') for link in apartment_links]

        # Use set difference to get only new ids
        unique_new_ids = set(new_ids) - set(all_ids)

        # Append new ids to all_ids and unique_ids
        all_ids += new_ids
        unique_ids.update(unique_new_ids)

    return all_ids