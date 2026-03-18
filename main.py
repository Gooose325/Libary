from operations import search_by_author, search_by_title
from Database import add_book_interactive, add_book, remove_book


start = input("Начать(да/нет): ").lower()
while start != "стоп":
    start = input("Продолжить(да/нет): ").lower()
    user = input("Напишите команду которую хотите выпполнить: ")
    if user == "Добавить книгу":
        my_books = []

        # Добавление книг
        while True:
            user_start = input("Добавить книгу? (да/нет): ").lower()
            if user_start == "нет":
                break
            else:
                add_book_interactive(my_books)

            print("-" * 40)
            print("Текущий список книг:")
            for book in my_books:
                print(f"Id: {book['id']}")
                print(f"Название: {book['title']}")
                print(f"Автор: {book['author']}")
                print(f"Год: {book['year']}")
                print("-" * 40)

            # Удаление книг
            while True:
                user_start = input("Удалить книгу? (да/нет): ").lower()
                if user_start == "нет":
                    break
                else:
                    while True:
                        book_id = input("Введите id книги: ").strip()
                        if book_id:
                            break
                        print("ID не может быть пустым. Попробуйте снова.")
                    remove_book(my_books, book_id)

            # Вывод списка
            while True:
                user_start = input("Вывести список? (да/нет): ").lower()
                if user_start == "нет":
                    break
                else:
                    print(my_books)

            # Поиск по автору
            while True:
                user_start = input("Поиск по автору? (да/нет): ").lower()
                if user_start == "нет":
                    break
                else:
                    author = input("Введите имя автора: ")
                    search_by_author(author, my_books)

            # Поиск по названию
            while True:
                user_start = input("Поиск по названию? (да/нет): ").lower()
                if user_start == "нет":
                    break
                else:
                    title = input("Введите название: ")
                    search_by_title(title, my_books)



