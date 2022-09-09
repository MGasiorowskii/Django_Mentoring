import requests

URL = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'

res = requests.get(url=URL)
data = res.json()

kind = data["kind"]
total_items = data["totalItems"]
items = data["items"]


# POST /db z body {"q": "war"}
URL = 'https://www.googleapis.com/books/v1/volumes'
PARAMS = {"q": "war"}

res = requests.get(url=URL, params=PARAMS)
data = res.json()

kind = data["kind"]
total_items = data["totalItems"]
items = data["items"]


# GET /books
structure = {
   "title": None,
   "authors": None,
   "published_date": None,
   "categories": None,
   "thumbnail": None,
}
result = []

for item in items:
    book = item["volumeInfo"]
    structure = structure.copy()

    structure['title'] = book.setdefault("title")
    structure['authors'] = book.setdefault("authors")
    structure["published_date"] = book.setdefault("publishedDate")
    structure["categories"] = book.setdefault("categories")
    structure["thumbnail"] = book["imageLinks"]["thumbnail"]

    result.append(structure)


# GET /books?author="Jan Kowalski"&author="Anna Kowalska"
structure = {
   "title": None,
   "authors": None,
   "published_date": None,
   "categories": None,
   "thumbnail": None,
}
result = []

for item in items:
    book = item["volumeInfo"]

    if book["authors"] == "Jan Kowalski" or book["authors"] == "Anna Kowalska":
        structure = structure.copy()

        structure['title'] = book.setdefault("title")
        structure['authors'] = book.setdefault("authors")
        structure["published_date"] = book.setdefault("publishedDate")
        structure["categories"] = book.setdefault("categories")
        structure["thumbnail"] = book["imageLinks"]["thumbnail"]

        result.append(structure)


# ET /books/<bookId>
structure = {
   "title": None,
   "authors": None,
   "published_date": None,
   "categories": None,
   "thumbnail": None,
}
result = []

bookid = "x38uAQAAIAAJ"

for item in items:
    if item['id'] == bookid:
        book = item["volumeInfo"]
        structure = structure.copy()

        structure['title'] = book.setdefault("title")
        structure['authors'] = book.setdefault("authors")
        structure["published_date"] = book.setdefault("publishedDate")
        structure["categories"] = book.setdefault("categories")
        structure["thumbnail"] = book["imageLinks"]["thumbnail"]

        result.append(structure)
