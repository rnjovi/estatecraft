import requests
import lxml
import cchardet
import datetime
from bs4 import BeautifulSoup
from scrape_apartment_ids import get_apartment_ids

def scrape_apartment_data(id):
    try:
        url = f"https://www.etuovi.com/kohde/{id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        # scrape the data you need using the BeautifulSoup functions

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
            return float(currency_str.translate(str.maketrans('', '', '\xa0,€')).strip())

        def convert_area(area_str):
            return float(area_str.split(" ")[0].replace(',', '.'))
        
        def convert_fee(price_str):
            return float(price_str.split(" ")[0].replace("\xa0€", "").replace(",", "."))
        
        def convert_to_int(string):
            return int(''.join(filter(str.isdigit, string)))
        
        id = id
        address = extract_info(soup, 'Sijainti', None)
        type = extract_info(soup, 'Tyyppi', None)

        price = extract_info(soup, 'Velaton hinta', '0')
        price = convert_currency(price)
        apartment_layout = extract_info(soup, 'Huoneistoselitelmä', None)

        living_area = extract_info(soup, 'Asuintilojen pinta-ala', '0')
        living_area = convert_area(living_area)

        floors = extract_info(soup, 'Kerrokset', None)
        year_of_construction = extract_info(soup, 'Rakennusvuosi', '0')
        year_of_construction = convert_to_int(year_of_construction)

        selling_price = extract_info(soup, 'Myyntihinta', '0')
        selling_price = convert_currency(selling_price)
        debt_share = extract_info(soup, 'Velkaosuus', '0')
        debt_share = convert_currency(debt_share)

        maintenance_fee = extract_info(soup, 'Hoitovastike', '0')
        maintenance_fee = convert_fee(maintenance_fee)
        
        financing_fee = extract_info(soup, 'Rahoitusvastike', '0')
        financing_fee  = convert_fee(financing_fee)

        sauna = extract_info(soup, 'Sauna', None)
        balcony = extract_info(soup, 'Parveke', None)
        elevator = extract_info(soup, 'Hissi', 'Ei hissiä')
        condition = extract_info(soup, 'Asunnon kunto', None)
        heating_system = extract_info(soup, 'Lämmitysjärjestelmän kuvaus', None)
        housing_company = extract_info(soup, 'Taloyhtiön nimi', None)
        energy_class = extract_info(soup, 'Energialuokka', None)
        lot_size = extract_info(soup, 'Tontin koko', None)
        ownership_type = extract_info(soup, 'Tontin omistus', None)
        renovation_info = extract_info(soup, 'Tehdyt remontit', None)
        future_renovations = extract_info(soup, 'Tulevat remontit', None)
        housing_company_id = extract_link(soup, 'Taloyhtiön nimi')
        date = datetime.date.today()

        apartment_info = (id, address, type, price, apartment_layout, living_area, floors, year_of_construction, 
        selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system,
        housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations, housing_company_id, date)
        return apartment_info

    except Exception as e:
        print(e)