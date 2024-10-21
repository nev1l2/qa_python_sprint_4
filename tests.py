import pytest

from conftest import collector
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

    # тестируем метод set_book_genre - добавляем жанр книге
    def test_set_book_genre_install_genre(self,collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.books_genre['Дюна'] == 'Фантастика'

    # тестируем метод get_book_genre - получаем жанр книги по её имени
    def test_get_book_genre_outputs_genre_by_name(self,collector_with_book):
        collector_with_book.get_book_genre('Дюна')
        assert collector_with_book.get_book_genre('Дюна') == 'Фантастика'

    # тестируем метод get_books_with_specific_genre - получаем список книг определенного жанра
    def test_get_books_with_specific_genre_shows_list_of_books_by_genre(self,collector_with_book):
        collector_with_book.get_books_with_specific_genre('Фантастика')
        assert len(collector_with_book.get_books_with_specific_genre('Фантастика')) == 2 and type(collector_with_book.get_books_with_specific_genre('Фантастика')) == list

    # тестируем метод get_books_genre - получаем словарь
    def test_get_books_genre_shows(self,collector_with_book):
        collector_with_book.get_books_genre()
        assert type(collector_with_book.get_books_genre()) == dict

    # тестируем метод get_books_for_children - получаем список подходящих для детей книг
    def test_get_books_for_children_display_list_without_genre_age_rating(self,collector_with_book):
        collector_with_book.get_books_for_children()
        assert len(collector_with_book.get_books_for_children()) == 3

    # тестируем метод add_book_in_favorites - добавление книги в избранное
    def test_add_book_in_favorites_add_one_book(self,collector_with_book):
        collector_with_book.add_book_in_favorites('Дюна')
        assert len(collector_with_book.favorites) == 1 and collector_with_book.favorites[0] == 'Дюна'

    # тестируем метод delete_book_from_favorites - удаление книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self,collector_with_book):
        collector_with_book.add_book_in_favorites('Дюна')
        collector_with_book.delete_book_from_favorites('Дюна')

        assert len(collector_with_book.favorites) == 0

    # тестируем метод get_list_of_favorites_books - проверяем что книга добавляется в избранное один раз и выводится списком
    def test_get_list_of_favorites_books_shows(self,collector_with_book):
        collector_with_book.add_book_in_favorites('Дюна')
        collector_with_book.add_book_in_favorites('Дюна')

        assert type(collector_with_book.get_list_of_favorites_books()) == list and len(collector_with_book.get_list_of_favorites_books()) == 1


    # ТЕСТЫ СОЗДАНЫ ДЛЯ ВЫПОЛНЕНИЯ ПУНКТА ЧЕК-ЛИСТА ЗАДАНИЯ "ПРИМЕНИТЬ ПАРАМЕТРИЗАЦИЮ"
    # тестируем метод add_new_book - проверяем КЭ и ГЗ - валидные
    @pytest.mark.parametrize('book_name', ['Я', 'Он','Вдаль от дома', 'Путешествия без границ: В поисках себя!'])
    def test_add_new_book_checking_the_entered_length_of_the_book_name(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    # тестируем метод add_new_book - проверяем КЭ и ГЗ - невалидные
    @pytest.mark.parametrize('book_name', ['', 'Путешествия без границ: В поисках себя настоящего!'])
    def test_add_new_book_book_name_with_an_invalide_length_is_not_added(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()