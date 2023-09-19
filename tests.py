from main import BooksCollector

import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Н', 'Не', 'Удивительные приключения Робинзона Круз', 'Удивительные приключения Робинзона Крузо', 'Удивительные приключ'])
    def test_add_new_book_add_book_with_length_in_range_from_1_to_41_book_added(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.books_genre) == 1 and list(collector.books_genre.keys()) == [name]

    @pytest.mark.parametrize('name', ['', 'Удивительные приключения Робинзона Крузо!', 'Необыкновенные и удивительные приключения Робинзона Крузо!'])
    def test_add_new_book_add_book_with_length_outside_range_from_1_to_41_book_no_added(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.books_genre) == 0

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_set_book_genre_add_book_and_set_genre_from_genre_list_genre_is_set(self):

        collector = BooksCollector()

        book_name = 'Зов Ктулху'
        book_genre = 'Ужасы'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert len(collector.books_genre) == 1 and collector.books_genre[book_name] == book_genre

    def test_set_book_genre_add_book_and_set_genre_not_from_genre_list_genre_is_not_set(self):

        collector = BooksCollector()

        book_name = 'Мастер и Маргарита'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Роман')

        assert collector.books_genre[book_name] == ''

    def test_get_book_genre_add_book_and_set_genre_get_books_genre_by_name(self):
        collector = BooksCollector()

        book_name = 'Зов Ктулху'
        book_genre = 'Ужасы'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_add_five_books_and_set_genres_get_books_with_expected_genre(self):

        collector = BooksCollector()

        books_with_genres = {
            'Зов Ктулху': 'Ужасы',
            'Непобедимый': 'Фантастика',
            'Ревизор': 'Комедии',
            'Туманность Андромеды': 'Фантастика',
            'Сказка про Колобка': 'Мультфильмы'
        }

        for book_name, book_genre in books_with_genres.items():
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_with_specific_genre('Фантастика') == ['Непобедимый', 'Туманность Андромеды']

    def test_get_books_genre_add_five_books_and_set_genres_get_books_with_genres(self):
        collector = BooksCollector()

        books_with_genres = {
            'Зов Ктулху': 'Ужасы',
            'Непобедимый': 'Фантастика',
            'Ревизор': 'Комедии',
            'Туманность Андромеды': 'Фантастика',
            'Сказка про Колобка': 'Мультфильмы'
        }

        for book_name, book_genre in books_with_genres.items():
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == books_with_genres

    @pytest.mark.parametrize('name, genre', [['Туманность Андромеды', 'Фантастика'], ['Ревизор', 'Комедии'], ['Сказка про Колобка', 'Мультфильмы']])
    def test_get_books_for_children_add_book_with_genre_for_children_book_added(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Приведение', 'Детективы']])
    def test_get_books_for_children_add_book_with_genre_from_genre_age_rating_list_book_no_added(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_book_in_favorites_book_added(self):
        collector = BooksCollector()

        book_name = 'Непобедимый'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert len(collector.favorites) == 1 and collector.favorites[0] == book_name

    def test_delete_book_from_favorites_add_and_delete_favorites_book_book_deleted(self):
        collector = BooksCollector()

        book_name = 'Непобедимый'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites(book_name)

        assert collector.favorites == []

    def test_get_list_of_favorites_books_add_three_books_in_favorites_get_added_books(self):
        collector = BooksCollector()

        book_names = ['В разреженном воздухе', 'Хоббит', 'Алиса в стране чудес']

        for book_name in book_names:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == book_names
