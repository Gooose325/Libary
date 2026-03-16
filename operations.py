def search_by_author(author, books):
    found_books = []
    for book in books:
        if author.lower() in book['author'].lower():
            found_books.append(book)

    if found_books:
        print(found_books)
    else:
        print("Книги этого автора не найдены.")


def search_by_title(title, books):
    found_books = []
    for book in books:
        if title.lower() in book['title'].lower():
            found_books.append(book)

    if found_books:
        print(found_books)
    else:

        print("Книги с таким названием не найдены.")
