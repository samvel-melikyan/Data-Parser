import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, url: str):
        self.url = url

    def take_data_from_web(self):
        page_num = 1
        data = []
        while True:
            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, 'lxml')
            entries = soup.find_all('div', class_= "article-summary-list")
            print(len(entries))

            for entry in entries:
                article_details = entry.find('div', class_="detail")
                article_title = article_details.find('h3').text
                article_date = article_details.find('time', class_ = "localtime-d-mmm-yyyy").text
                article_text = article_details.find('p').text
                article_writer = article_details.find('span', class_='displayname').find('a').text
                article_cotegory = article_details.find('div', class_ = "rubric article-category").find('a').text


                data.append({'title': article_title, 'cotegory': article_cotegory , 'writer': article_writer, 'date': article_date, 'text': article_text[:25]+"..."})

            page_num += 1

            if len(entries) != 0:
                break

        return data


    def write_data(self):
        pass
url = "https://letterboxd.com/journal/archive/"
data =  Parser(url)
print(data.take_data_from_web())