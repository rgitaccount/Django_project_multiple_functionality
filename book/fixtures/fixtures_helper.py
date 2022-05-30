import urllib.request
import requests
from bs4 import BeautifulSoup
import json


URL = "https://reedsy.com/discovery/blog/best-books-to-read-in-a-lifetime"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="book-blot")
    books = []
    for item in items:
        books.append(
            {
                "title": item.find("em").get_text(),
                "author": item.find("h2").get_text().split('by ')[1],
                "description": item.find("div", class_="blurb").get_text(strip=True),
                "image": item.find("img").get("data-srcset"),
                "image_name": item.find("em").get_text().replace(" ", "_" ) + '.jpg'
            }
        )
    return books


def download_image(url, file_path, file_name):
    full_path = file_path + file_name
    urllib.request.urlretrieve(url, full_path)


if __name__ == "__main__":
    html = get_html(URL)
    books = get_data(html.text)

    # # Download images
    # for book in books:
    #     download_image(book["image"],
    #                    "../../media/",
    #                    book["image_name"])
    #     print(book["title"])

    authors_to_dump = [{"model": "book.author", "pk": index+1, "fields":
        {
            "first_name": value["author"].split(" ")[0],
            "last_name": value["author"].split(" ")[-1],
            "date_of_birth": "2022-05-18",
            "date_of_death": "2022-05-18"
        }} for index, value in enumerate(books)]

    json_authors = json.dumps(authors_to_dump, indent=4)
    with open("authors.json", "w") as outfile:
        outfile.write(json_authors)


    books_to_dump = [{"model": "book.book", "pk": index+1, "fields":
        {
            "title": value["title"],
            "author": index+1,
            "description": value["description"],
            "created_date": "2022-05-18",
            "updated_date": "2022-05-18",
            "image": f'/{value["image_name"]}',
        }} for index, value in enumerate(books)]


    json_books = json.dumps(books_to_dump, indent=4)
    with open("books.json", "w") as outfile:
        outfile.write(json_books)

    download_image("https://m.media-amazon.com/images/I/31ijiaTuJzL._SL160_.jpg",
                   "../../media/", "name")
