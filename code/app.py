from scrape_apartment_ids import get_apartment_ids
from database import Database
from scrape_apartment_data import Scraper

if __name__ == '__main__':
    db = Database()

    # Drop and recreate table if needed (testing only, should be commented out)
    # db.drop_and_create_apartments()

    # Get the list of ids from the function get_apartment_ids
    ids = get_apartment_ids()

    # Get the list of ids that are already in the database
    ids_in_db = db.get_all_ids()

    # Remove the ids that are already in the database from the list of ids
    ids_to_scrape = [id for id in ids if id not in ids_in_db]

    scraper = Scraper()
    scraper.start_scraping(ids_to_scrape)
