import requests
from bs4 import BeautifulSoup
from scrape_apartment_ids import get_apartment_ids
from database import Database


# Create a new database connection
db = Database(dbname="real_estate_info", user="postgres", password=SECRET_PASSWORD)


def create_table():
    # Drops table for testing purposes.
    db.execute("DROP TABLE apartments")

    # Creates table
    db.execute('''CREATE TABLE apartments
            (id INTEGER PRIMARY KEY,
            address TEXT,
            type TEXT,
            price TEXT,
            apartment_layout TEXT,
            living_area TEXT,
            floors TEXT,
            year_of_construction TEXT,
            selling_price TEXT,
            debt_share TEXT,
            maintenance_fee TEXT,
            financing_fee TEXT,
            sauna TEXT,
            balcony TEXT,
            elevator TEXT,
            condition TEXT,
            heating_system TEXT,
            housing_company TEXT,
            energy_class TEXT,
            lot_size TEXT,
            ownership_type TEXT,
            renovation_info TEXT,
            future_renovations TEXT,
            link TEXT)''')

    
def scrape_apartment_data(id):
    try:
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

        id = int(id)
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
        link = "https://www.etuovi.com/" + extract_link(soup, 'Taloyhtiön nimi')

        apartment_info = (id, address, type, price, apartment_layout, living_area, floors, year_of_construction, 
        selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system,
        housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations, link)
        return apartment_info

    except Exception as e:
        print(e)


def save_data(apartment_info):
    query = '''INSERT INTO apartments (id, address, type, price, apartment_layout, living_area, floors, year_of_construction, selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system, housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations, link)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    db.execute(query, apartment_info)

def view_table():
    # Create a cursor
    cur = db.conn.cursor()

    # Execute a SELECT statement
    cur.execute("SELECT * FROM apartments")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.conn.close()
    

if __name__ == '__main__':
    ids = get_apartment_ids()

    # Only for 1 card
    data = scrape_apartment_data(ids[0])
    # For all cards
    """
    for id in ids:
            data = scrape_apartment_data(id)
            print()
    """
    create_table()
    save_data(data)
    view_table()