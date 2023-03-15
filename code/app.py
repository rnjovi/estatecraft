from runtime_measures import measure_get_apartment_ids_runtime, measure_scrape_apartment_data_runtime
from table_creation import create_apartments_table

def main():
    # measure the runtime of get_apartment_ids
    ids = measure_get_apartment_ids_runtime()

    # create a table to store the scraped data
    create_apartments_table()

    # scrape data for each apartment ID
    measure_scrape_apartment_data_runtime(ids)

if __name__ == '__main__':
    main()