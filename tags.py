import requests 
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc= f.read()

soup= BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())

# print(soup.title.string, type(soup.title.string))
# print(soup.div)
# print(soup.find_all("a"))

# for link in soup.find_all("a"):
#     print(link.get("href"))

# print(soup.find(id="link1"))
# print(soup.select("div.italic"))
# print(soup.select("div#italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_= "footer").children:
#     print(child)
#     # This if printed with type is alternate navigable string and tag

# for parent in soup.find(id= "link1").parents:
#     print(parent)

#Modification of existing tags
container = soup.find(class_= "footer")
container.name= "div"
container["class"]= "newClassName anotherClassName"
container.string= "New data as constituent of this class"
print(container)
# This changes the dom currently. It doesn't cause changes in original sample.html file but we can either generate a new file with updated DOM or we can also replace the file with new DOM