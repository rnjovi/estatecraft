import requests
from bs4 import BeautifulSoup
import datetime
from concurrent.futures import ThreadPoolExecutor
from scrape_apartment_ids import get_apartment_ids

# Web scraping
class Scraper:
    def __init__(self):
        self.ids = get_apartment_ids()

    def extract_info(self, soup, search_term, default='-'):
        try:
            info = soup.find('div', string=search_term).find_next_sibling('div').text.strip()
        except AttributeError:
            info = default
        return info

    def extract_link(self, soup, search_term, default=''):
        try:
            element = soup.find('div', string=search_term).find_next_sibling('div').find('a')
            info = element['href']
            info = info.rsplit('/', 1)[-1]
        except (AttributeError, TypeError):
            info = default
        return info

    def scrape_apartment_data(self, id):
        try:
            url = f"https://www.etuovi.com/kohde/{id}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            id = id
            address = self.extract_info(soup, 'Sijainti', '-')
            type = self.extract_info(soup, 'Tyyppi', '-')
            price = self.extract_info(soup, 'Velaton hinta', '')
            apartment_layout = self.extract_info(soup, 'Huoneistoselitelmä', '-')
            living_area = self.extract_info(soup, 'Asuintilojen pinta-ala', '-')
            floors = self.extract_info(soup, 'Kerrokset', '-')
            year_of_construction = self.extract_info(soup, 'Rakennusvuosi', '-')
            year_of_construction = year_of_construction[:4]
            selling_price = self.extract_info(soup, 'Myyntihinta', '')
            debt_share = self.extract_info(soup, 'Velkaosuus', '')
            maintenance_fee = self.extract_info(soup, 'Hoitovastike', '')
            financing_fee = self.extract_info(soup, 'Rahoitusvastike', '')
            sauna = self.extract_info(soup, 'Sauna', '-')
            balcony = self.extract_info(soup, 'Parveke', '-')
            elevator = self.extract_info(soup, 'Hissi', 'Ei hissiä')
            condition = self.extract_info(soup, 'Asunnon kunto', '-')
            heating_system = self.extract_info(soup, 'Lämmitysjärjestelmän kuvaus', '-')
            housing_company = self.extract_info(soup, 'Taloyhtiön nimi', '-')
            energy_class = self.extract_info(soup, 'Energialuokka', '-')
            lot_size = self.extract_info(soup, 'Tontin koko', '-')
            ownership_type = self.extract_info(soup, 'Tontin omistus', '-')
            renovation_info = self.extract_info(soup, 'Tehdyt remontit', '-')
            future_renovations = self.extract_info(soup, 'Tulevat remontit', '-')
            housing_company_id = self.extract_link(soup, 'Taloyhtiön nimi')
            added_date = datetime.date.today()
            deleted_date = None

            apartment_info = (id, address, type, price, apartment_layout, living_area, floors, year_of_construction, 
            selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system,
            housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations, housing_company_id, added_date, deleted_date)
            return apartment_info

        except Exception as e:
            print(e)

    def start_scraping(self, ids):
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.scrape_apartment_data, ids)