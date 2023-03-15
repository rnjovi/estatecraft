from config import TYPE_KEYWORD, LOCATION_KEYWORD
from utils.runtime_measures import measure_get_apartment_ids_runtime, measure_scrape_apartment_data_runtime
from database.table_creation import create_apartments_table
from database.queries import run_queries


def main():
    """
    Main function to run the application, including measuring runtime,
    creating the apartments table, scraping apartment data, and running queries.
    """

    # Measure the runtime of the get_apartment_ids function and store the apartment IDs
    ids = measure_get_apartment_ids_runtime()

    # Create a table in the database to store the scraped apartment data
    create_apartments_table()

    # Scrape data for each apartment ID and measure the runtime of the scrape_apartment_data function
    measure_scrape_apartment_data_runtime(ids)

    # Run queries on the apartment data using the specified type and location keywords
    run_queries(TYPE_KEYWORD, LOCATION_KEYWORD)


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()