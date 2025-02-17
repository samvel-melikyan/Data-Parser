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

## Example Output
The output Excel file (articles.xlsx) will contain the following columns:

Title: The title of the article.
Date: The publication date of the article (in YYYY-MM-DD format).
Category: The category of the article (e.g., review, list).
Writer: The name of the article's author.
Text: A brief excerpt from the article.

Example Data in Excel:
### Explanation:
- The table is formatted using **Markdown** syntax, which will display neatly when rendered in GitHub or similar markdown readers.
- The columns are separated by vertical bars (`|`) and the header row is followed by a separator line with dashes (`-`).

This will create a properly formatted table in your `README.md` file, as shown below:

| Title                          | Date       | Category | Writer       | Text                                      |
|--------------------------------|------------|----------|--------------|-------------------------------------------|
| My Favorite Films of 2025      | 2025-02-16 | Review   | John Doe     | A deep dive into the films that made 2025 a standout year for cinema... |
| Best Cinematic Moments         | 2025-02-15 | List     | Jane Smith   | Here are the top 10 cinematic moments that defined this year... |
| A Look Back at 2024's Hits     | 2025-02-14 | Review   | Michael Lee  | Reflecting on the hits and misses from last year in the film industry... |

This is the correct Markdown formatting for your table to appear visually structured in the `README.md` file. Let me know if you need anything else!
