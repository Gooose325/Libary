import operations
import Database


start = input("Напишите команду которую хотите выпполнить")
while start != "стоп":
    if start == "Добавить книгу":
        Database.Books()


