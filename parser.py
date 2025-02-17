import requests
from bs4 import BeautifulSoup
import pandas as pd


class Parser:
    """ A class to scrape article data from the Letterboxd journal archive pages."""

    def take_data_from_web(self):
        """Scrapes articles from the Letterboxd journal archive pages.

        Iterates through all the journal archive pages and extracts article
        information such as title, date, text, category, and writer.
        The function stops when there are no more articles to scrape.

        Returns:
            list: A list of dictionaries containing the article details."""
        page_num = 1
        data = []

        while True:
            print(page_num, end=' ')
            html_content = requests.get(f'https://letterboxd.com/journal/archive/page/{page_num}/').text
            soup = BeautifulSoup(html_content, 'lxml')
            entries = soup.find_all('article', class_= "article-summary -inline-teaser")

            for entry in entries:
                try:
                    article_details = entry.find('div', class_="detail")
                    article_title = article_details.find('h3').text
                    article_date = article_details.find('time', class_="localtime-d-mmm-yyyy").get('datetime', 'No Date Found')[:10]
                    article_text = article_details.find('p').text #[:25] + "..."
                    article_cotegory = article_details.find('div', class_="rubric article-category").find('a').text
                    article_writer = article_details.find('span', class_='displayname').find('a').text
                except AttributeError:
                    pass

                data.append({'title': article_title,
                             'date': article_date,
                             'category': article_cotegory,
                             'writer': article_writer,
                             'text': article_text})
            page_num += 1
            if len(entries) == 0:
                break
        return data


    def write_data(self):
        """Writes the scraped article data to an Excel file.

        This method collects data using `take_data_from_web()` and writes the
        resulting list of dictionaries into an Excel file named 'articles.xlsx'."""
        df = pd.DataFrame(self.take_data_from_web())
        df.to_excel('articles.xlsx')





url = "https://letterboxd.com/journal/archive/"
data =  Parser()
data.write_data()
# print(data.take_data_from_web())


