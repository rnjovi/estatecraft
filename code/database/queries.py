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
        AVG(CASE WHEN ownership_type ILIKE 'vuokra%%' THEN maintenance_fee END) as avg_maintenance_fee_vuokra,
        AVG(CASE WHEN ownership_type ILIKE 'oma%%' THEN maintenance_fee END) as avg_maintenance_fee_oma,
        AVG(financing_fee),
        AVG(CASE WHEN ownership_type ILIKE 'vuokra%%' THEN price END) as avg_price_vuokra,
        AVG(CASE WHEN ownership_type ILIKE 'oma%%' THEN price END) as avg_price_oma
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
        'avg_maintenance_fee_vuokra': row[11],
        'avg_maintenance_fee_oma': row[12],
        'avg_financial_fee': row[13],
        'avg_price_vuokra': row[14],
        'avg_price_oma': row[15]
    } for row in results]

def run_queries():
    type_keyword = "Kerrostalo"
    location_keyword = "Pirkkala"
    count = count_type_in_location(type_keyword, location_keyword)
    print()
    print(f"There are {count} apartments of type '{type_keyword}' for sale in addresses containing '{location_keyword}'.")
    layout_infos = count_layouts_by_type_and_location("Kerrostalo", "Pirkkala")
    
    for info in layout_infos:
        print()
        print(f"Layout: {info['layout']}")
        print(f"  Count: {info['count']}")
        print(f"  Average price: {info['avg_price']:.2f}")
        print(f"  Average living area: {info['avg_living_area']:.2f}")
        print(f"  Cheapest apartment: {info['min_price']}")
        print(f"  Most expensive apartment: {info['max_price']}")
        print(f"  Smallest living area: {info['min_living_area']}")
        print(f"  Largest living area: {info['max_living_area']}")
        print(f"  Average year of construction: {info['avg_year_of_construction']:.2f}")
        print(f"  Average selling price: {info['avg_selling_price']:.2f}")
        print(f"  Average debt share: {info['avg_debt_share']:.2f}")
        print(f"  Average maintenance fee (Vuokra): {info['avg_maintenance_fee_vuokra']:.2f}")
        print(f"  Average maintenance fee (Oma): {info['avg_maintenance_fee_oma']:.2f}")
        print(f"  Average financial fee: {info['avg_financial_fee']:.2f}")
        print(f"  Average price (Vuokra): {info['avg_price_vuokra']:.2f}")
        print(f"  Average price (Oma): {info['avg_price_oma']:.2f}")