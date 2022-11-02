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
        return f" 1:{news[0].text};\n 2:{news[1].text};\n 3:{news[2].text};\n 4:{news[3].text};\n 5:{news[4].text};\n"








