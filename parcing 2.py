import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://kenesh.kg/ru/news/all/list'

def write_to_csv(data):
    with open('news2title.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['date_'], data['image'], data['description']])

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    list_news = soup.find_all('div', class_ = 'news__item news__item__3')
    for news in list_news:
        title = news.find('h3').text.strip()
        description = news.find('p',class_="news__item__desc").text if news.find('p') != None else news.find('a', class_="news__item__title__link").text
        date_ = news.find('div', class_ = 'news__item__date').text
        image = news.find('img').get('src') if news.find('img') != None else 'No image in the article'
        dict_ = {'title':title, 'image':image, 'date_': date_, 'description': description}
        write_to_csv(dict_)

def main():
    count = 1

    for i in range(20):
        news_url = f'http://kenesh.kg/ru/news/all/list?page={str(count)}'
        get_data(get_html(news_url))
    count += 21

main()
