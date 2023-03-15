from timeit import default_timer as timer
from scraping.scrape_apartment_data import scrape_apartment_data
from scraping.scrape_apartment_ids import get_apartment_ids
from database.table_creation import save_data, filter_existing_ids

def measure_get_apartment_ids_runtime():
    """
    Measure the runtime of get_apartment_ids function and return the IDs.

    :return: List of apartment IDs
    """
    start = timer()
    ids = get_apartment_ids()
    end = timer()
    runtime = end - start
    print(f"get_apartment_ids runtime: {runtime} seconds")
    return ids

def measure_scrape_apartment_data_runtime(ids):
    """
    Measure the runtime of scrape_apartment_data for each apartment ID,
    print statistics, and save the data to the database.

    :param ids: List of apartment IDs to scrape
    """
    # Remove existing IDs from the list before scraping
    ids = filter_existing_ids(ids)

    # If there are no new IDs to scrape, print a message and return
    if not ids:
        print("All IDs are already in the database. No new apartments to scrape.")
        return

    total_scrape_time = 0
    count = 1
    for id in ids:
        start = timer()
        data = scrape_apartment_data(id)
        end = timer()
        if data is not None:  # Data is None when an exception occurs during scraping
            save_data(data)

        total_scrape_time += (end - start)
        print(count)
        count += 1

    avg_scrape_time = total_scrape_time / len(ids)
    print(f"Scraped {len(ids)} apartments")
    print(f"Average time per apartment scrape: {avg_scrape_time} seconds")
    print(f"The total time of scrape: {total_scrape_time}")
