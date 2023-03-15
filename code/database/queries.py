from database import Database

db = Database(dbname="real_estate_info", user="postgres", password="new_password")

def count_type_in_location(type_keyword, location_keyword):
    query = f"""SELECT COUNT(*) FROM apartments
                WHERE type LIKE %s AND address LIKE %s;"""
    result = db.fetch_one(query, (f"%{type_keyword}%", f"%{location_keyword}%"))
    return result[0]

def run_queries():
    type_keyword = "Kerrostalo"
    location_keyword = "Pirkkala"
    count = count_type_in_location(type_keyword, location_keyword)
    print(f"There are {count} apartments of type '{type_keyword}' for sale in addresses containing '{location_keyword}'.")
