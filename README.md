# Real Estate Analysis Project

This project scrapes real estate data and performs analysis on apartment sales in Finland. The main goal is to provide useful insights and statistics for different types of apartments and locations.

## Features

- Scrapes apartment data from online sources
- Stores the scraped data in a PostgreSQL database
- Performs analysis on the data, such as:
  - Counting apartments of a specific type in a location
  - Calculating average prices, living area, and other statistics
  - Comparing data between different types of apartments (e.g., owned vs. rented)

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Installation

1. Clone the repository:

git clone https://github.com/rnjovi/estatecraft.git

2. Change to the project directory:

cd real_estate_analysis


3. Install the required Python packages:

pip install -r requirements.txt


4. Set up the PostgreSQL database by providing the necessary credentials in the `config.py` file.

### Usage

To run the project, execute the `app.py` script:

python app.py


This will start the scraping process, store the data in the database, and run the analysis queries.

## Contributing

If you'd like to contribute to this project, feel free to submit pull requests or open issues on GitHub.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
