from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

yc_content = soup.find(name="span", class_="titleline")
content_text = yc_content.getText()
content_link = yc_content.get("a")



print(content_text)
print(content_link)

