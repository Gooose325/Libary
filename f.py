from seacher import my_books

#Поиск книги по автору
def search_by_author(author):
    found_books = []
    if author.lower() in my_books['author'].lower():
        found_books.append(my_books)
        return print(found_books)

#Поиск книги по названию
def search_by_title(title):
    found_books = []
    if title.lower() in my_books['author'].lower():
        found_books.append(my_books)
        return print(found_books)




