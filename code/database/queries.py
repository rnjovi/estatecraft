from database.database import Database

db = Database(dbname="real_estate_info", user="postgres", password="new_password")

def count_type_in_location(type_keyword, location_keyword):
    query = f"""SELECT COUNT(*) FROM apartments
                WHERE type LIKE %s AND address LIKE %s;"""
    result = db.fetch_one(query, (f"%{type_keyword}%", f"%{location_keyword}%"))
    return result[0]

def count_layouts_by_type_and_location(type_keyword, location_keyword):
    query = '''
    SELECT
        CASE
            WHEN apartment_layout ILIKE '1h%%' THEN '1h'
            WHEN apartment_layout ILIKE '2h%%' THEN '2h'
            WHEN apartment_layout ILIKE '3h%%' THEN '3h'
            WHEN apartment_layout ILIKE '4h%%' THEN '4h'
            ELSE 'Else'
        END as layout,
        COUNT(*)
    FROM apartments
    WHERE type ILIKE %s AND address ILIKE %s
    GROUP BY layout
    HAVING (
        CASE
            WHEN apartment_layout ILIKE '1h%%' THEN '1h'
            WHEN apartment_layout ILIKE '2h%%' THEN '2h'
            WHEN apartment_layout ILIKE '3h%%' THEN '3h'
            WHEN apartment_layout ILIKE '4h%%' THEN '4h'
            ELSE 'Else'
        END IN ('1h', '2h', '3h', '4h', 'Else')
    )
    ORDER BY layout
    '''

    results = db.fetch(query, (f"%{type_keyword}%", f"%{location_keyword}%"))

    return {row[0]: row[1] for row in results}

def run_queries():
    type_keyword = "Kerrostalo"
    location_keyword = "Pirkkala"
    count = count_type_in_location(type_keyword, location_keyword)
    print()
    print(f"There are {count} apartments of type '{type_keyword}' for sale in addresses containing '{location_keyword}'.")
    counts = count_layouts_by_type_and_location("Kerrostalo", "Pirkkala")
    print(counts)
