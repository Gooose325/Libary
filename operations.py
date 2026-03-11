# Убран импорт my_books для устранения циклического импорта
# Функции теперь принимают список книг как аргумент

def search_by_author(author, books):
    found_books = []
    for book in books:
        # Исправлено: перебор списка и правильное обращение к ключу
        if author.lower() in book['author'].lower():
            found_books.append(book)

    if found_books:
        print(found_books)
    else:
        print("Книги этого автора не найдены.")
    # return found_books # Лучше возвращать список, а не print


def search_by_title(title, books):
    found_books = []
    for book in books:
        # Исправлено: проверка поля 'title', а не 'author'
        if title.lower() in book['title'].lower():
            found_books.append(book)

    if found_books:
        print(found_books)
    else:
        print("Книги с таким названием не найдены.")