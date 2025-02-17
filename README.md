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

<table border="1">
  <thead>
    <tr>
      <th>Title</th>
      <th>Date</th>
      <th>Category</th>
      <th>Writer</th>
      <th>Text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>My Favorite Films of 2025</td>
      <td>2025-02-16</td>
      <td>Review</td>
      <td>John Doe</td>
      <td>A deep dive into the films that made 2025 a standout year for cinema...</td>
    </tr>
    <tr>
      <td>Best Cinematic Moments</td>
      <td>2025-02-15</td>
      <td>List</td>
      <td>Jane Smith</td>
      <td>Here are the top 10 cinematic moments that defined this year...</td>
    </tr>
    <tr>
      <td>A Look Back at 2024's Hits</td>
      <td>2025-02-14</td>
      <td>Review</td>
      <td>Michael Lee</td>
      <td>Reflecting on the hits and misses from last year in the film industry...</td>
    </tr>
  </tbody>
</table>
