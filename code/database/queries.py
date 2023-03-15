from .database import Database

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
        COUNT(*),
        AVG(price),
        AVG(living_area),
        MIN(price),
        MAX(price),
        MIN(living_area),
        MAX(living_area),
        AVG(year_of_construction),
        AVG(selling_price),
        AVG(debt_share),
        AVG(maintenance_fee),
        AVG(financing_fee)
    FROM apartments
    WHERE type ILIKE %s AND address ILIKE %s
    GROUP BY layout
    ORDER BY layout
    '''

    results = db.fetch(query, (f"%{type_keyword}%", f"%{location_keyword}%"))

    return [{
        'layout': row[0],
        'count': row[1],
        'avg_price': row[2],
        'avg_living_area': row[3],
        'min_price': row[4],
        'max_price': row[5],
        'min_living_area': row[6],
        'max_living_area': row[7],
        'avg_year_of_construction': row[8],
        'avg_selling_price': row[9],
        'avg_debt_share': row[10],
        'avg_maintenance_fee': row[11],
        'avg_financing_fee': row[12]
    } for row in results]

def run_queries():
    type_keyword = "Kerrostalo"
    location_keyword = "Pirkkala"
    count = count_type_in_location(type_keyword, location_keyword)
    print()
    print(f"There are {count} apartments of type '{type_keyword}' for sale in addresses containing '{location_keyword}'.")
    counts = count_layouts_by_type_and_location("Kerrostalo", "Pirkkala")

    # Print the individual counts and additional information in separate rows
    print("\nApartment layout details:")
    for info in counts:
        print(f"{info['layout']}:")
        print(f"  Count: {info['count']}")
        print(f"  Average price: {info['avg_price']:.2f}")
        print(f"  Average living area: {info['avg_living_area']:.2f}")
        print(f"  Cheapest apartment: {info['min_price']}")
        print(f"  Most expensive apartment: {info['max_price']}")
        print(f"  Smallest living area: {info['min_living_area']}")
        print(f"  Biggest living area: {info['max_living_area']}")
        print(f"  Average year of construction: {info['avg_year_of_construction']:.1f}")
        print(f"  Average selling price: {info['avg_selling_price']:.2f}")
        print(f"  Average debt share: {info['avg_debt_share']:.2f}")
        print(f"  Average maintenance fee: {info['avg_maintenance_fee']:.2f}")
        print(f"  Average financing fee: {info['avg_financing_fee']:.2f}")
        print()