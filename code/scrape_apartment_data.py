import requests
import lxml
import cchardet
import datetime
from bs4 import BeautifulSoup
from dataclasses import dataclass


def extract_info(soup, search_term, default=None):
    try:
        info = soup.find('div', string=search_term).find_next_sibling('div').text.strip()
    except AttributeError:
        info = default
    return info

def extract_link(soup, search_term, default='-'):
    try:
        info = soup.find('div', string=search_term).find_next_sibling('div').find('a')['href']
        info = info.split("/")
    except (AttributeError, TypeError):
        info = default
    return info[-1]

def convert_currency(currency_str):
    return float(currency_str.replace('\xa0', '').replace(',', '.').strip('€').strip())

def convert_area(area_str):
    return float(area_str.split(" ")[0].replace(',', '.'))

def convert_fee(price_str):
    cleaned_price_str = price_str.split(" ")[0].replace("\xa0", "").replace("€", "").replace(",", ".")
    return float(cleaned_price_str)

def convert_to_int(string):
    return int(''.join(filter(str.isdigit, string)))



@dataclass
class ApartmentInfo:
    id: str
    address: str
    type: str
    price: float
    apartment_layout: str
    living_area: float
    floors: str
    year_of_construction: int
    selling_price: float
    debt_share: float
    maintenance_fee: float
    financing_fee: float
    sauna: str
    balcony: str
    elevator: str
    condition: str
    heating_system: str
    housing_company: str
    energy_class: str
    lot_size: str
    ownership_type: str
    renovation_info: str
    future_renovations: str
    housing_company_id: str
    date: datetime.date


def scrape_apartment_data(id):
    try:
        url = f"https://www.etuovi.com/kohde/{id}"

        with requests.get(url) as response:
            soup = BeautifulSoup(response.content, 'lxml')

            # Use separate functions to extract each element
            id = id
            address = extract_address(soup)
            type = extract_type(soup)
            price = extract_price(soup)
            apartment_layout = extract_apartment_layout(soup)
            living_area = extract_living_area(soup)
            floors = extract_floors(soup)
            year_of_construction = extract_year_of_construction(soup)
            selling_price = extract_selling_price(soup)
            debt_share = extract_debt_share(soup)
            maintenance_fee = extract_maintenance_fee(soup)
            financing_fee = extract_financing_fee(soup)
            sauna = extract_sauna(soup)
            balcony = extract_balcony(soup)
            elevator = extract_elevator(soup)
            condition = extract_condition(soup)
            heating_system = extract_heating_system(soup)
            housing_company = extract_housing_company(soup)
            energy_class = extract_energy_class(soup)
            lot_size = extract_lot_size(soup)
            ownership_type = extract_ownership_type(soup)
            renovation_info = extract_renovation_info(soup)
            future_renovations = extract_future_renovations(soup)
            housing_company_id = extract_housing_company_id(soup)
            date = datetime.date.today()

            apartment_info = ApartmentInfo(
                id, address, type, price, apartment_layout, living_area, floors, year_of_construction, selling_price,
                debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system,
                housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations,
                housing_company_id, date
            )

            return apartment_info

    except Exception as e:
        print(e)
        return None  # Add this line to return None in case of an exception

def extract_address(soup):
    return extract_info(soup, 'Sijainti', None)

def extract_type(soup):
    return extract_info(soup, 'Tyyppi', None)

def extract_price(soup):
    price = extract_info(soup, 'Velaton hinta', '0')
    return convert_currency(price)

def extract_apartment_layout(soup):
    return extract_info(soup, 'Huoneistoselitelmä', None)

def extract_living_area(soup):
    living_area = extract_info(soup, 'Asuintilojen pinta-ala', '0')
    return convert_area(living_area)

def extract_floors(soup):
    return extract_info(soup, 'Kerrokset', None)

def extract_year_of_construction(soup):
    year_of_construction = extract_info(soup, 'Rakennusvuosi', '0')
    return convert_to_int(year_of_construction)

def extract_selling_price(soup):
    selling_price = extract_info(soup, 'Myyntihinta', '0')
    return convert_currency(selling_price)

def extract_debt_share(soup):
    debt_share = extract_info(soup, 'Velkaosuus', '0')
    return convert_currency(debt_share)

def extract_maintenance_fee(soup):
    maintenance_fee = extract_info(soup, 'Hoitovastike', '0')
    return convert_fee(maintenance_fee)

def extract_financing_fee(soup):
    financing_fee = extract_info(soup, 'Rahoitusvastike', '0')
    return convert_fee(financing_fee)

def extract_sauna(soup):
    return extract_info(soup, 'Sauna', None)

def extract_balcony(soup):
    return extract_info(soup, 'Parveke', None)

def extract_elevator(soup):
    return extract_info(soup, 'Hissi', 'Ei hissiä')

def extract_condition(soup):
    return extract_info(soup, 'Asunnon kunto', None)

def extract_heating_system(soup):
    return extract_info(soup, 'Lämmitysjärjestelmän kuvaus', None)

def extract_housing_company(soup):
    return extract_info(soup, 'Taloyhtiön nimi', None)

def extract_energy_class(soup):
    return extract_info(soup, 'Energialuokka', None)

def extract_lot_size(soup):
    return extract_info(soup, 'Tontin koko', None)

def extract_ownership_type(soup):
    return extract_info(soup, 'Tontin omistus', None)

def extract_renovation_info(soup):
    return extract_info(soup, 'Tehdyt remontit', None)

def extract_future_renovations(soup):
    return extract_info(soup, 'Tulevat remontit', None)

def extract_housing_company_id(soup):
    return extract_link(soup, 'Taloyhtiön nimi')