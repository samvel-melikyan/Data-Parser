# Data-Parsing
# Letterboxd Journal Scraper

This Python script is used to scrape articles from the Letterboxd journal archive. The scraper collects article data such as the title, date, category, writer, and text, and then writes the collected data into an Excel file.

## Features

- Scrapes multiple pages from the Letterboxd journal archive.
- Extracts article details: title, date, text, category, and writer.
- Saves the collected data to an Excel file (`articles.xlsx`).
  
## Requirements

- Python 3 and higher
- `requests` library for making HTTP requests.
- `beautifulsoup4` library for parsing HTML.
- `pandas` library for saving data to Excel.

You can install the required libraries by running:

```bash
pip install requests beautifulsoup4 pandas openpyxl

