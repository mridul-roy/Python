from bs4 import BeautifulSoup


with open(file="website.html", encoding="utf8")as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.find_all())