from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(name='a', rel='noreferrer')
print(article_tag.getText())

# print(soup.find_all('a'))

# with open(file="website.html", encoding="utf8")as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.find_all())
