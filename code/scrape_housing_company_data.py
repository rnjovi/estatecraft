import requests
from bs4 import BeautifulSoup

"""
Work to do with browser interaction, because data i need is hidden.

"""

def get_page_content(url):
    """Fetch the content of the url page"""
    response = requests.get(url)
    response.raise_for_status() # Will raise an error if the GET request was unsuccessful
    return BeautifulSoup(response.content, 'html.parser')

def parse_company_info(soup):
    """Parse the company's name and address from the soup object"""
    company_info_div = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 mui-style-1547ak')
    company_name = company_info_div.find('h1').text.strip()
    address_parts = company_info_div.find('h2').text.strip().split(',')
    postal_code = address_parts[0].strip()
    city = address_parts[1].strip()
    return company_name, postal_code, city

def parse_div_elements(soup):
    """Parse specific div elements from the soup object"""
    div_elements = soup.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-3 mui-style-9ttabb')
    results = []
    for div in div_elements:
        label_element = div.find('div', class_='MuxA_7k')
        value_element = div.find('div', class_='uYggTa9')
        if label_element and value_element:
            label = label_element.text.strip()
            value = value_element.text.strip()
            results.append((label, value))
    return results

def parse_additional_elements(soup):
    """Parse additional div elements from the soup object"""
    div_elements = soup.find_all('div', {'class': 'wmmykQT'})
    return [div_element.get_text(strip=True) for div_element in div_elements]

def scrape_housing_company_data():
    url = "https://etuovi.com/myytavat-asunnot/taloyhtiot/2263211-3/"
    soup = get_page_content(url)
    
    company_name, postal_code, city = parse_company_info(soup)
    print(company_name)
    print(postal_code)
    print(city)

    div_elements = parse_div_elements(soup)
    for label, value in div_elements:
        print(f"{label}: {value}")

    additional_elements = parse_additional_elements(soup)
    for text in additional_elements:
        print(text)

if __name__ == '__main__':
    scrape_housing_company_data()
