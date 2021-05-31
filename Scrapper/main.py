from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
# # all_a = soup.find_all(name = 'a')
# # for tag in all_a:
# #     # print(tag.getText())
# #     print(tag.get('href'))

# # heading = soup.find(name = 'h1', id = 'name')
# # print(heading)

# # section_heading = soup.find(name = 'h3', class_ = 'heading')
# # print(section_heading)

# '''CSS selector'''
# # company_url = soup.select_one(selector = 'p a')
# # print(company_url)

# # item1 = soup.select_one(selector = '#name')
# # print(item1)

# item2 = soup.select('.heading')
# print(item2)

'''Scraping news from [https://news.ycombinator.com/news]'''
#https://news.ycombinator.com/robots.txt

# response = requests.get("https://news.ycombinator.com/news")
# yc_page = response.text
# soup = BeautifulSoup(yc_page, "html.parser")
# article_tag = soup.find_all(name = 'a', class_ = 'storylink')
# article_texts = []
# article_links = []
# for article in article_tag:
#     article_text = article.getText()
#     article_texts.append(article_text)
#     article_link = article.get('href')
#     article_links.append(article_link)

# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name = 'span', class_ = 'score')]

# print(article_texts[article_upvote.index(max(article_upvote))])

'''Scraping news from [https://www.empireonline.com/movies/features/best-movies-2/]'''

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

