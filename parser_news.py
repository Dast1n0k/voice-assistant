import requests
from bs4 import BeautifulSoup as BS
r = requests.get("https://www.pravda.com.ua/news/")
html = BS(r.content, 'html.parser')

# for el in html.select(".tile-list-wr > .movie-block"):
#     title = el.find('div', class_='movie-block__mobile-name').get_text(strip=True)
#     href = el.find('div', class_='movie-block__mobile-name').find('a').get('href')
#     films = {}
#     films[title] = str(href)
#     print(films)


def parser_news():
    for el in html.select(".main_content"):
        news = el.select('.article_header > a')
        return f"\n {news[0].text};\n {news[1].text};\n {news[2].text};\n {news[3].text};\n {news[4].text};\n"


