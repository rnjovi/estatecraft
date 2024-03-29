import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from lxml import html
from config import SEARCH_KEY

MAX_WORKERS = 12

def create_session():
    """
    Create and return a new requests.Session with a custom User-Agent header.
    """
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    return session

def get_total_pages(session, base_url, query_string):
    """
    Return the total number of pages for the given query string using the provided requests.Session.
    """
    first_page_url = f"{base_url}?{query_string}&sivu=1"
    response = session.get(first_page_url)
    soup = BeautifulSoup(response.content, 'lxml')

    elements = soup.find_all('button', {'class': 'theme__button__1YqFK theme__flat__13aFK theme__button__1YqFK theme__squared__17Uvn theme__neutral__1F1Jf Button__button__3K-jn Pagination__button__3H2wX'})
    last_element = elements[-1] if elements else None
    total_pages = int(last_element.text.strip()) if last_element else 1

    return total_pages

def fetch_and_parse_page(session, base_url, query_string, page_num):
    """
    Fetch a specific page and parse it to extract apartment IDs.
    """
    current_page_url = f"{base_url}?{query_string}&sivu={page_num}"
    response = session.get(current_page_url)
    soup = BeautifulSoup(response.content, 'lxml')
    apartment_links = soup.find_all('div', {'class': 'ListPage__cardContainer__39dKQ'})

    new_ids = [link.find('a', {'class': 'mui-style-58tli6 e12nd9f313'}).get('id') for link in apartment_links]
    return new_ids

def get_apartment_ids():
    """
    Scrape and return a list of unique apartment IDs based on the search key from the config.
    """
    base_url = 'https://www.etuovi.com/myytavat-asunnot'
    query_string = 'haku=' + SEARCH_KEY

    session = create_session()
    total_pages = get_total_pages(session, base_url, query_string)
    unique_ids = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        fetch_and_parse = lambda page_num: fetch_and_parse_page(session, base_url, query_string, page_num)
        for new_ids in executor.map(fetch_and_parse, range(1, total_pages + 1)):
            unique_ids += new_ids

    return unique_ids