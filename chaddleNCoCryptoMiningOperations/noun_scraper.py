import requests
from bs4 import BeautifulSoup
from pprint import pprint

page = requests.get("https://www.momswhothink.com/list-of-nouns/")

soup = BeautifulSoup(page.content, "html.parser")
#lists_scraped = soup.find_all("ul")

for ul in soup.find_all('ul'):
    for idx, li in enumerate(ul.findChildren('li')):
        stripped = str(li).replace(" ", "").replace("<li>", "").replace("</li>", "")
        if len(stripped) < 32:
            print(stripped.capitalize())
            with open("custom_nouns.txt", "a+") as f:
                f.write(f"{stripped.capitalize()}\n")
# for idx, li in enumerate(lists_scraped):
#     if idx in range(3):
#         print(li)
#pprint(lists_scraped)
