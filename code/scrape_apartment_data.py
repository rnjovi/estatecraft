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

    apartment_info = []

    address = extract_info(soup, 'Sijainti', '-')
    type = extract_info(soup, 'Tyyppi', '-')
    price = extract_info(soup, 'Velaton hinta', '-')
    apartment_layout = extract_info(soup, 'Huoneistoselitelmä', '-')
    living_area = extract_info(soup, 'Pinta-ala', '-')
    floors = extract_info(soup, 'Kerros', '-')
    year_of_construction = extract_info(soup, 'Rakennusvuosi', '-')
    selling_price = extract_info(soup, 'Myyntihinta', '-')
    debt_share = extract_info(soup, 'Velkaosuus', '-')
    maintenance_fee = extract_info(soup, 'Hoitovastike', '-')
    financing_fee = extract_info(soup, 'Rahoitusvastike', '-')
    sauna = extract_info(soup, 'Sauna', '-')
    balcony = extract_info(soup, 'Parveke', '-')
    elevator = extract_info(soup, 'Hissi', '-')
    condition = extract_info(soup, 'Kunto', '-')
    heating_system = extract_info(soup, 'Lämmitysjärjestelmä', '-')
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

if __name__ == '__main__':
    ids = get_apartment_ids()

    data = scrape_apartment_data(ids[0])

    """
    for id in ids:
            data = scrape_apartment_data(id)
            print()
    """
    
