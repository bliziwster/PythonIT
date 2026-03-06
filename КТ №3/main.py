import csv_parser as cp
from functools import reduce


def demonstrate_all_tasks():

    books = cp.get_books("books.csv")
    cp.print_books_table(books, "Задание 1: Все книги")

    filtered = cp.filtered_books(books, "python")
    cp.print_books_table(filtered, "Задание 2: Книги с 'python' в названии")

    totals = cp.get_totals(filtered)
    print("\nЗадание 3: Общая стоимость:")
    print("-" * 40)

    list(
        map(
            lambda item: print(f"ISBN: {item[0]}, Total: ${item[1]:.2f}"),
            totals
        )
    )


def main():

    demonstrate_all_tasks()

    input("\nНажмите Enter для выхода...")


if __name__ == "__main__":
    main()