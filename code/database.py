import pypyodbc as odbc

password="Testitalo1"
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:apartments-finland.database.windows.net,1433;Database=apartmets-finland;Uid=CloudSA63c3246d;Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

class Database:
    def __init__(self):
        self.conn = odbc.connect(connection_string)
        self.cursor = self.conn.cursor()

    def get_all_ids(self):
        query = "SELECT id FROM apartments"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return [row[0] for row in result]

    def insert_apartment_data(self, apartment_info):
        query = '''INSERT INTO apartments (
                    id, address, type, price, apartment_layout, living_area, floors, year_of_construction, 
                    selling_price, debt_share, maintenance_fee, financing_fee, sauna, balcony, elevator, condition, 
                    heating_system, housing_company, energy_class, lot_size, ownership_type, renovation_info, 
                    future_renovations, housing_company_id, added_date, deleted_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(query, apartment_info)
        self.conn.commit()

    def drop_and_create_apartments(self):
        self.cursor.execute("DROP TABLE IF EXISTS apartments")
        self.cursor.execute('''
            CREATE TABLE apartments (
                id NVARCHAR(255) PRIMARY KEY,
                address NVARCHAR(255),
                type NVARCHAR(255),
                price NVARCHAR(255),
                apartment_layout NVARCHAR(255),
                living_area NVARCHAR(255),
                floors NVARCHAR(255),
                year_of_construction INT,
                selling_price NVARCHAR(255),
                debt_share NVARCHAR(255),
                maintenance_fee NVARCHAR(255),
                financing_fee NVARCHAR(255),
                sauna NVARCHAR(255),
                balcony NVARCHAR(255),
                elevator NVARCHAR(255),
                condition NVARCHAR(255),
                heating_system NVARCHAR(MAX),
                housing_company NVARCHAR(255),
                energy_class NVARCHAR(255),
                lot_size NVARCHAR(255),
                ownership_type NVARCHAR(255),
                renovation_info NVARCHAR(MAX),
                future_renovations NVARCHAR(MAX),
                housing_company_id NVARCHAR(255),
                added_date DATETIME,
                deleted_date DATETIME
            )
        ''')
        self.conn.commit()
        print("#done")
