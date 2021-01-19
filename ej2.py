import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost')
    db =client.get_database('examen')
    col = db['webscraping']


    response = requests.get("https://www.elsevier.com/es-es/connect")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="tile-image-anchor")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title['title'],
            'link'  : post_title['href']
        })

   
    for post in extracted:
        if col.find_one({'link': post['link']}) is None:
            print("Found a new listing at the following url: ", post['link'])
            col.insert(post)
            