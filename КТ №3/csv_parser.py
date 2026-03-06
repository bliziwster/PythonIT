import csv
from typing import List, Tuple, Any, Callable
from functools import reduce


def read_csv_file(filename: str) -> List[List[str]]:

    with open(filename, 'r', encoding='utf-8') as file:

        lines = file.readlines()

        cleaned_lines = list(
            map(lambda line: line.strip().split('|'), lines)
        )

        non_empty_lines = list(
            filter(lambda line: len(line) > 1, cleaned_lines)
        )
        
        return non_empty_lines


def parse_value(value: str) -> Any:

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value


def parse_row(row: List[str]) -> List[Any]:

    return list(
        map(parse_value, row)
    )


def get_books(filename: str) -> List[List[Any]]:

    all_rows = read_csv_file(filename)

    data_rows = list(
        map(parse_row, all_rows[1:])
    )
    
    return data_rows


def contains_substring(substring: str) -> Callable[[List[Any]], bool]:

    def check_book(book: List[Any]) -> bool:

        return substring.lower() in book[1].lower()
    
    return check_book


def transform_book(book: List[Any]) -> List[Any]:

    return [
        book[0], 
        f"{book[1]}, {book[2]}", 
        book[3],  
        book[4]   
    ]


def filtered_books(books: List[List[Any]], substring: str) -> List[List[Any]]:

    filtered = list(
        filter(contains_substring(substring), books)
    )

    transformed = list(
        map(transform_book, filtered)
    )
    
    return transformed


def calculate_total_price(book: List[Any]) -> Tuple[str, float]:

    return (book[0], book[2] * book[3])


def get_totals(books: List[List[Any]]) -> List[Tuple[str, float]]:

    return list(
        map(calculate_total_price, books)
    )


def compose(*functions: Callable) -> Callable:

    def compose_two(f: Callable, g: Callable) -> Callable:
        return lambda x: f(g(x))
    
    return reduce(compose_two, functions, lambda x: x)


def print_books_table(books: List[List[Any]], title: str = "Books") -> None:

    print(f"\n{title}:")
    print("-" * 80)
    for book in books:
        print(book)