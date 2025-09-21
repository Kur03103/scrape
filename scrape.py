# python -m pip install requests
# 
# python -m pip install beautifulsoup4

# git config -- global user.name "Aayush Sapkota"
# git config -- global user.email "aayushaj3103@gmail.com"

#git init
#git status => if you want to check what are the status of the file
#git diff => if you want to check what are the changes
#git add .
#git commit -m "Finish Project"
# copy paste git code from github

###############
# 1. change the code
# 2. git add
# 3. git commit -m "Your message"
# 4. git push

import json
import requests 
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrive the page.")
        return 

    # Set encoding explicitly to handle special character
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    all_books = []

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_= 'price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        all_books.append(
            {
                "title":title,
                "currency":currency,
                "price":price,
            }
        )
    return all_books

books = scrape_books(url)

with open("books.json", "w", encoding='utf-8') as f:
    json.dump(books, f, indent = 2, ensure_ascii=False)

    

