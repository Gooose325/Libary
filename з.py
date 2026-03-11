import uuid

def add_book_interactive(books: List[Dict]) -> Dict:
    # Запрашиваем название
    while True:
        title = input("Введите название книги: ").strip()
        if title:
            break
        print(" Название не может быть пустым. Попробуйте снова.")

    # Запрашиваем автора
    while True:
        author = input("Введите автора книги: ").strip()
        if author:
            break
        print(" Автор не может быть пустым. Попробуйте снова.")

    # Запрашиваем год с проверкой корректности
    while True:
        try:
            year = int(input("Введите год издания: "))
            if 0 < year <= 2100:
                break
            else:
                print(" Год должен быть между 1 и 2100. Попробуйте снова.")
        except ValueError:
            print(" Ошибка: введите целое число.")

    # Запрашиваем жанр
    while True:
        genre = input("Введите жанр книги: ").strip()
        if genre:
            break
        print(" Жанр не может быть пустым. Попробуйте снова.")

    # СОЗДАЁМ КНИГУ И ДОБАВЛЯЕМ В КОЛЛЕКЦИЮ
    book = {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'year': year,
        'genre': genre
    }

    books.append(book)
    print(f" Книга '{title}' успешно добавлена с ID {book['id']}.")

    return book


def add_book(books: List[Dict], title: str, author: str, year: int, genre: str) -> Dict:
    book = {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'year': year,
        'genre': genre
    }

    books.append(book)
    print(f" Книга '{title}' успешно добавлена с ID {book['id']}.")

    return book
my_books = []
while True:
    user_start = input("Добавить книгу?").lower()
    if user_start == "нет":
        break
    else:
        add_book_interactive(my_books)


print("-" * 40)
for book in my_books:
    print(f"Id: {book['id']}")
    print(f"Название: {book['title']}")
    print(f"Автор: {book['author']}")
    print(f"Год: {book['year']}")
    print("-" * 40)


def remove_book(my_books: List[Dict], book_id: str) -> bool:


  # Перебираем все книги в поиске нужного ID
 for i, book in enumerate(my_books):
     if book['id'] == book_id:

 # Удаляем книгу из списка
         removed_book = my_books.pop(i)
         print(f" Книга '{removed_book['title']}' (ID: {book_id}) успешно удалена.")
         return True

 # Если книга не найдена
 print(f" Книга с ID {book_id} не найдена.")
 return False


while True:
    user_start = input("Удалить книгу?").lower()
    if user_start == "нет":
        break
    else:
     while True:
      book_id = input("Введите id книги: ").strip()
      if book_id:
       break
      print(" Название не может быть пустым. Попробуйте снова.")
      remove_book(my_books, book_id)

while True:
    user_start = input("Вывести список?").lower()
    if user_start == "нет":
        break
    else:
        print(my_books)