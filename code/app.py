from config import TYPE_KEYWORD, LOCATION_KEYWORD
from utils.runtime_measures import measure_get_apartment_ids_runtime, measure_scrape_apartment_data_runtime
from database.table_creation import create_apartments_table
from database.queries import run_queries


def main():
    """
    Main function to run the application, including measuring runtime,
    creating the apartments table, scraping apartment data, and running queries.
    """

    # measure the runtime of get_apartment_ids
    ids = measure_get_apartment_ids_runtime()

    # create a table to store the scraped data
    create_apartments_table()

    # scrape data for each apartment ID
    measure_scrape_apartment_data_runtime(ids)

    # Run queries
    run_queries(TYPE_KEYWORD, LOCATION_KEYWORD)


if __name__ == '__main__':
    main()