import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from lxml import html

def get_apartment_ids():
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=M1955542998'

    # Create a session object for reusing the underlying TCP connection
    session = requests.Session()

    # Get the number of pages from the first page of the search results
    first_page_url = f"{base_url}?{query_string}&sivu=1"
    response = session.get(first_page_url)
    soup = BeautifulSoup(response.content, 'lxml')

    elements = soup.find_all('button', {'class': 'theme__button__1YqFK theme__flat__13aFK theme__button__1YqFK theme__squared__17Uvn theme__neutral__1F1Jf Button__button__3K-jn Pagination__button__3H2wX'})
    last_element = elements[-1] if elements else None
    value = int(last_element.text.strip()) if last_element else 1

    unique_ids = []

    def fetch_and_parse_page(page_num):
        current_page_url = f"{base_url}?{query_string}&sivu={page_num}"
        response = session.get(current_page_url)
        soup = BeautifulSoup(response.content, 'lxml')
        apartment_links = soup.find_all('div', {'class': 'ListPage__cardContainer__39dKQ'})

        # Use list comprehension to extract apartment ids
        new_ids = [link.find('a', {'class': 'mui-style-58tli6 e12nd9f313'}).get('id') for link in apartment_links]
        return new_ids

    # Use ThreadPoolExecutor to parallelize fetching and parsing webpages
    with ThreadPoolExecutor() as executor:
        for new_ids in executor.map(fetch_and_parse_page, range(1, value+1)):
            unique_ids += new_ids

    return unique_ids