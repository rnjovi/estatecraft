from database import Database

import multiprocessing as mp

# Create a new database connection
db = Database(dbname="real_estate_info", user="postgres", password="new_password")


def create_apartments_table():
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
    db.execute(query, (
        apartment_info.id, apartment_info.address, apartment_info.type, apartment_info.price, apartment_info.apartment_layout,
        apartment_info.living_area, apartment_info.floors, apartment_info.year_of_construction, apartment_info.selling_price,
        apartment_info.debt_share, apartment_info.maintenance_fee, apartment_info.financing_fee, apartment_info.sauna,
        apartment_info.balcony, apartment_info.elevator, apartment_info.condition, apartment_info.heating_system,
        apartment_info.housing_company, apartment_info.energy_class, apartment_info.lot_size, apartment_info.ownership_type,
        apartment_info.renovation_info, apartment_info.future_renovations, apartment_info.housing_company_id, apartment_info.date
    ))

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
