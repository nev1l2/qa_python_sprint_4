import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_book():
    collector = BooksCollector()
    for name in ['Дюна', 'Оно', 'Задача трех тел', 'Смешарики']:
        collector.add_new_book(name)
    collector.set_book_genre('Смешарики', 'Мультфильмы')
    collector.set_book_genre('Дюна', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Задача трех тел', 'Фантастика')
    return collector
