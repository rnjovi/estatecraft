import cProfile
import pstats
from scrape_apartment_data import scrape_apartment_data
from scrape_apartment_ids import get_apartment_ids
from database import Database


# Create a new database connection
db = Database(dbname="real_estate_info", user="postgres", password="new_password")


def create_table():
    # Drops table for testing purposes.
    db.execute("DROP TABLE apartments")

    # Creates table
    db.execute('''CREATE TABLE apartments
            (id VARCHAR(10) PRIMARY KEY,
            address TEXT,
            type TEXT,
            price FLOAT,
            apartment_layout TEXT,
            living_area FLOAT,
            floors TEXT,
            year_of_construction INT,
            selling_price FLOAT,
            debt_share FLOAT,
            maintenance_fee FLOAT,
            financing_fee FLOAT,
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
            housing_company_id VARCHAR(10),
            date TEXT
            )''')

def save_data(apartment_info):
    query = '''INSERT INTO apartments (id, address, type, price, apartment_layout, living_area, floors, year_of_construction, selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, heating_system, housing_company, energy_class, lot_size, ownership_type, renovation_info, future_renovations, housing_company_id, date)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    db.execute(query, *apartment_info)

def sql_query(query):
    # Create a cursor
    cur = db.conn.cursor()

    # Execute statement
    cur.execute(query)

    # Fetch all rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.conn.close() 

if __name__ == '__main__':
    with cProfile.Profile() as profile:
        ids = get_apartment_ids()

        create_table()

        # Only for 1 card
        # data = scrape_apartment_data(ids[0])
        # For all cards
        c = 1
        for id in ids:
                data = scrape_apartment_data(id)
                save_data(data)
                print(c)
                c = c + 1
        
        # sql_query("SELECT * FROM apartments")
    
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()