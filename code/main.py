import cProfile
import pstats
from scrape_apartment_data import scrape_apartment_data
from scrape_apartment_ids import get_apartment_ids
from table_creation import create_table, save_data, sql_query

if __name__ == '__main__':
    # get the list of apartment IDs to scrape
    ids = get_apartment_ids()

    # create a table to store the scraped data
    create_table()

    # scrape data for each apartment ID
    apartment_data = []
    c = 1
    for id in ids:
        data = scrape_apartment_data(id)
        apartment_data.append(data)
        save_data(data)
        print(c)
        c = c + 1

    # sql_query("SELECT * FROM apartments")
