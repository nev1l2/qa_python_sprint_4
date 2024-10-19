import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector_with_book(self):
        collector = BooksCollector()
        for name in ['Дюна', 'Оно', 'Задача трех тел', 'Смешарики']:
            collector.add_new_book(name)
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Задача трех тел', 'Фантастика')
        return collector

    def test_set_book_genre_install_genre(self,collector_with_book):
        assert collector_with_book.books_genre['Дюна'] == 'Фантастика'

    def test_get_book_genre_outputs_genre_by_name(self,collector_with_book):
        assert collector_with_book.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_shows_list_of_books_by_genre(self,collector_with_book):
        assert len(collector_with_book.get_books_with_specific_genre('Фантастика')) == 2 and type(collector_with_book.get_books_with_specific_genre('Фантастика')) == list

    def test_get_books_genre_shows(self,collector_with_book):
        assert type(collector_with_book.get_books_genre()) == dict

    def test_get_books_for_children_display_list_without_genre_age_rating(self,collector_with_book):
        assert len(collector_with_book.get_books_for_children()) == 3

    @pytest.mark.parametrize('book_name', ['Дюна', 'Оно', 'Смешарики'])
    def test_add_book_in_favorites_add_one_book(self,collector_with_book, book_name):
        collector_with_book.add_book_in_favorites(book_name)

        assert len(collector_with_book.favorites) == 1 and collector_with_book.favorites[0] == book_name

    def test_delete_book_from_favorites_delete_one_book(self,collector_with_book):
        collector_with_book.delete_book_from_favorites('Дюна')

        assert len(collector_with_book.favorites) == 0

    def test_get_list_of_favorites_books_shows(self,collector_with_book):
        collector_with_book.add_book_in_favorites('Дюна')
        collector_with_book.add_book_in_favorites('Оно')

        assert type(collector_with_book.get_list_of_favorites_books()) == list

    @pytest.mark.parametrize('book_name', ['Я', 'Он','Вдаль от дома', 'Путешествия без границ: В поисках себя!'])
    def test_add_new_book_checking_the_entered_length_of_the_book_name(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', ['', 'Путешествия без границ: В поисках себя настоящего!'])
    def test_add_new_book_book_name_with_an_invalide_length_is_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()