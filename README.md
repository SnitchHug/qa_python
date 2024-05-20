main.py - класс BooksCollector
test.py - тестовый класс BooksCollector
conftest.py - фикстуры

Проверки в test.py:
test_add_new_book_add_two_books - добаление книг в словарь
test_add_new_book_out_of_range_name_is_not_added - добавление книг с количеством символов: 0, 41, 42
test_set_book_genre_added - добавление жанра к книге
test_get_books_with_specific_genre_displayed_book - вывод книги определенного жанра
test_get_books_for_children_displayed_list - вывод списка книг для детей
test_add_book_in_favorites_is_added - добавление книги в список избранное
test_add_book_in_favorites_not_added - добавление книги не из словаря в список избранное
test_delete_book_from_favorites_deleted_book - удаление книги из списка избранное
test_delete_book_from_favorites_not_deleted_book - удаление книги не из списка избранное