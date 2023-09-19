## Unit тесты для методов класса BooksCollector

___

1. Тесты для проверки метода `add_new_book()`:

    - `test_add_new_book_add_book_with_length_in_range_from_1_to_41_book_added()` - проверяет, что книги с длиной названия от 1 до 41 (не включая) символа добавляются в словарь `books_genre` (параметризированный тест).

    - `test_add_new_book_add_book_with_length_outside_range_from_1_to_41_book_no_added()` - проверяет, что книги с длиной названия равной 0 или >= 41 символа не добавляются в словарь `books_genre` (параметризированный тест).

    - `test_add_new_book_add_two_books()` - проверяет, что в словарь `books_genre` добавляются названия двух книг.


2. Тесты для проверки метода `set_book_genre()`:

    - `test_set_book_genre_add_book_and_set_genre_from_genre_list_genre_is_set()` - проверяет, что книге, добавленной в словарь `books_genre`, устанавливается жарн из списка доступных жанров `genre`.

    - `test_set_book_genre_add_book_and_set_genre_not_from_genre_list_genre_is_not_set()` -  проверяет, что книге, добавленной в словарь `books_genre`, не устанавливается жанр, который отсутствует в списке доступных жанров `genre`.


3. Тест для проверки метода `get_book_genre()` (получение жанра книги по названию):

    `test_get_book_genre_add_book_and_set_genre_get_books_genre_by_name()` - проверяет, что метод `get_book_genre()` возвращает жанр книги, который соответствует установленному жанру.


4. Тест для проверки метода `get_books_with_specific_genre()`:

    `test_get_books_with_specific_genre_add_five_books_and_set_genres_get_books_with_expected_genre()` - проверяет, что полученный список названий книг с определённым жанром соответствует ожидаемому списку.


5. Тест для проверки метода `get_books_genre()`:

    `test_get_books_genre_add_five_books_and_set_genres_get_books_with_genres()` - проверяет, что полученный из метода `get_books_genre()` словарь `books_genre` соответствует исходному словарю с тестовыми данными для добавления названия книг и установки жанров.


6. Тесты для проверки метода `get_books_for_children()`:

    - `test_get_books_for_children_add_book_with_genre_for_children_book_added` - проверяет, что название книги с установленным жанром, который отсутствует в списке жанров с ограничением по возрасту, добавляется в список книг, подходящий детям (параметризированный тест).

    - `test_get_books_for_children_add_book_with_genre_from_genre_age_rating_list_book_no_added` - проверяет, что название книги с установленным жанром, который присутствует в списке жанров с ограничением по возрасту, не добавляется в список книг, подходящий детям(параметризированный тест).


7. Тест для проверки метода `add_book_in_favorites()`:

    `test_add_book_in_favorites_add_book_in_favorites_book_added` - проверяет, что название книги добавляется в список Избранное.


8. Тест для проверки метода `delete_book_from_favorites()`:

    `test_delete_book_from_favorites_add_and_delete_favorites_book_book_deleted` - проверяет, что добавленное название книги в Избранное удалается из списка Избранное.


9. Тест для проверки метода `get_list_of_favorites_books()`:

    `test_get_list_of_favorites_books_add_three_books_in_favorites_get_added_books` - проверяет, что метод `get_list_of_favorites_books()` возвращает список названий книг, который соответсвует добавленным в Избранное книгам.