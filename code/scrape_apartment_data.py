import requests

from bs4 import BeautifulSoup
from scrape_apartment_ids import get_apartment_ids

def scrape_apartment_data(id):
    url = f"https://www.etuovi.com/kohde/{id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # scrape the data you need using the BeautifulSoup functions

    def extract_info(soup, search_term, default='-'):
        try:
            info = soup.find('div', string=search_term).find_next_sibling('div').text.strip()
        except AttributeError:
            info = default
        return info

    def extract_link(soup, search_term, default='-'):
        try:
            info = soup.find('div', string=search_term).find_next_sibling('div').find('a')['href']
        except (AttributeError, TypeError):
            info = default
        return info

    apartment_info = []

    address = extract_info(soup, 'Sijainti', '-')
    type = extract_info(soup, 'Tyyppi', '-')
    price = extract_info(soup, 'Velaton hinta', '-')
    apartment_layout = extract_info(soup, 'Huoneistoselitelmä', '-')
    living_area = extract_info(soup, 'Asuintilojen pinta-ala', '-')
    floors = extract_info(soup, 'Kerrokset', '-')
    year_of_construction = extract_info(soup, 'Rakennusvuosi', '-')
    selling_price = extract_info(soup, 'Myyntihinta', '-')
    debt_share = extract_info(soup, 'Velkaosuus', '0')
    maintenance_fee = extract_info(soup, 'Hoitovastike', '-')
    financing_fee = extract_info(soup, 'Rahoitusvastike', '0')
    sauna = extract_info(soup, 'Sauna', '-')
    balcony = extract_info(soup, 'Parveke', '-')
    elevator = extract_info(soup, 'Hissi', 'Ei hissiä')
    condition = extract_info(soup, 'Asunnon kunto', '-')
    heating_system = extract_info(soup, 'Lämmitysjärjestelmän kuvaus', '-')
    housing_company = extract_info(soup, 'Taloyhtiön nimi', '-')
    energy_class = extract_info(soup, 'Energialuokka', '-')
    lot_size = extract_info(soup, 'Tontin koko', '-')
    ownership_type = extract_info(soup, 'Tontin omistus', '-')
    renovation_info = extract_info(soup, 'Tehdyt remontit', '-')
    future_renovations = extract_info(soup, 'Tulevat remontit', '-')

    apartment_info.append(address)
    apartment_info.append(type)
    apartment_info.append(price)
    apartment_info.append(apartment_layout)
    apartment_info.append(living_area)
    apartment_info.append(floors)
    apartment_info.append(year_of_construction)
    apartment_info.append(selling_price)
    apartment_info.append(debt_share)
    apartment_info.append(maintenance_fee)
    apartment_info.append(financing_fee)
    apartment_info.append(sauna)
    apartment_info.append(balcony)
    apartment_info.append(elevator)
    apartment_info.append(condition)
    apartment_info.append(heating_system)
    apartment_info.append(housing_company)
    apartment_info.append(energy_class)
    apartment_info.append(lot_size)
    apartment_info.append(ownership_type)
    apartment_info.append(renovation_info)
    apartment_info.append(future_renovations)

    for elem in apartment_info:
        print(elem)

    link = "https://www.etuovi.com/" + extract_link(soup, 'Taloyhtiön nimi')
    print(link)


if __name__ == '__main__':
    ids = get_apartment_ids()

    data = scrape_apartment_data(ids[0])

    url = "https://www.etuovi.com/myytavat-asunnot/pirkkala/loukonlahti/taloyhtiot/0218164-2/asunto-oy-korkeakallio"

    # Send a request to the URL and get the response
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with class "MobileTable__row__1xkd0"
    rows = soup.find_all('div', {'class': 'MobileTable__row__1xkd0'})

    # Create an empty 2D list to store the scraped data
    data = []

    # Loop through each row and scrape the values
    for row in rows:
        # Find all div elements with class "MobileTable__alwaysVisibleCells__YQGaa" in the current row
        cells = row.find_all('div', {'class': 'MobileTable__alwaysVisibleCells__YQGaa'})
        
        # Extract the values from the cells and append them to the data list
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
        
    # Print the scraped data
    print(data)

    """
    for id in ids:
            data = scrape_apartment_data(id)
            print()
    """
    
