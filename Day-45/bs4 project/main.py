from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# all_anchor_tag = soup.find_all(name="a")
#
# for tag in all_anchor_tag :
#     print(tag.get("href"))

heading = soup.find(name="h3", class_="heading")

print(heading)