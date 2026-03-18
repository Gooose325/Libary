import uuid
from typing import List, Dict
from operations import search_by_title, search_by_author


def add_book_interactive(books: List[Dict]) -> Dict:
    # Запрашиваем название
    while True:
        title = input("Введите название книги: ").strip()
        if title:
            break
        print("Название не может быть пустым. Попробуйте снова.")

    # Запрашиваем автора
    while True:
        author = input("Введите автора книги: ").strip()
        if author:
            break
        print("Автор не может быть пустым. Попробуйте снова.")

    # Запрашиваем год с проверкой корректности
    while True:
        try:
            year = int(input("Введите год издания: "))
            if 0 < year <= 2100:
                break
            else:
                print("Год должен быть между 1 и 2100. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите целое число.")

    # Запрашиваем жанр
    while True:
        genre = input("Введите жанр книги: ").strip()
        if genre:
            break
        print("Жанр не может быть пустым. Попробуйте снова.")

    # СОЗДАЁМ КНИГУ И ДОБАВЛЯЕМ В КОЛЛЕКЦИЮ
    book = {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'year': year,
        'genre': genre
    }

    books.append(book)
    print(f"Книга '{title}' успешно добавлена с ID {book['id']}.")

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
    print(f"Книга '{title}' успешно добавлена с ID {book['id']}.")
    return book


def remove_book(books: List[Dict], book_id: str) -> bool:
    # Исправлены комментарии (добавлен #)
    # Перебираем все книги в поиске нужного ID
    for i, book in enumerate(books):
        if book['id'] == book_id:
            # Удаляем книгу из списка
            removed_book = books.pop(i)
            print(f"Книга '{removed_book['title']}' (ID: {book_id}) успешно удалена.")
            return True
    # Если книга не найдена
    print(f"Книга с ID {book_id} не найдена.")
    return False


