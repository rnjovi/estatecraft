from timeit import default_timer as timer
from scrape_apartment_data import scrape_apartment_data
from scrape_apartment_ids import get_apartment_ids
from table_creation import create_table, save_data, sql_query

if __name__ == '__main__':
    # measure the runtime of get_apartment_ids
    start = timer()
    ids = get_apartment_ids()
    end = timer()
    runtime = end - start
    print(f"get_apartment_ids runtime: {runtime} seconds")

    # calculate the average time per ID
    avg_time_per_id = runtime / len(ids)
    print(f"Average time per ID: {avg_time_per_id} seconds")

    """
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

    """


    # sql_query("SELECT * FROM apartments")