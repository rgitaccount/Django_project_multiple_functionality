import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt


HOST = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
HOST_2 = "https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction/"

HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
}


@csrf_exempt
def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("tr", {'itemtype': 'http://schema.org/Book'})
    goodreads_list = []

    for item in items:
        goodreads_list.append(
            {
                "link": "https://www.goodreads.com" + item.find("a").get("href"),
                "title": item.find("a", class_="bookTitle").get_text().strip(),
                "image": item.find("img").get("src")
            }
        )

    return goodreads_list


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        return get_data(html.text)
    else:
        raise Exception("Error in parser function")


@csrf_exempt
def get_data_nyt(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", class_="css-13y32ub")
    nyt_list = []
    for item in items:
        nyt_list.append(
            {
                "link": item.find("a", class_="css-114t425").get("href"),
                "title": item.find("h3", {"itemprop": "name"}).get_text(),
                "image": item.find("img", {"itemprop": "image"}).get("src")
            }
        )
    return nyt_list


@csrf_exempt
def parser_func_nyt():
    html = get_html(HOST_2)
    if html.status_code == 200:
        nyt_list = get_data_nyt(html.text)
        return nyt_list
    else:
        raise Exception("Error in parser function Nyt")







