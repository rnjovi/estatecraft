from timeit import default_timer as timer
from scrape_apartment_data import scrape_apartment_data
from scrape_apartment_ids import get_apartment_ids
from table_creation import create_apartments_table, save_data, sql_query

def measure_get_apartment_ids_runtime():
    start = timer()
    ids = get_apartment_ids()
    end = timer()
    runtime = end - start
    print(f"get_apartment_ids runtime: {runtime} seconds")
    return ids

def measure_scrape_apartment_data_runtime(ids):
    total_scrape_time = 0
    for id in ids:
        start = timer()
        data = scrape_apartment_data(id)
        end = timer()
        save_data(data)
        total_scrape_time += (end - start)
    avg_scrape_time = total_scrape_time / len(ids)
    print(f"Scraped {len(ids)} apartments")
    print(f"Average time per apartment scrape: {avg_scrape_time} seconds")

def main():
    # measure the runtime of get_apartment_ids
    ids = measure_get_apartment_ids_runtime()

    # create a table to store the scraped data
    create_apartments_table()

    # scrape data for each apartment ID
    measure_scrape_apartment_data_runtime(ids)

    # sql_query("SELECT * FROM apartments")

if __name__ == '__main__':
    main()