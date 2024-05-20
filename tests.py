import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book',
                             ['',
                              'ШестьШестьШестьШестьШестьШестьШестьШестьЩ',
                              'ШестьШестьШестьШестьШестьШестьШестьШестьШе']
                             )
    def test_add_new_book_out_of_range_name_is_not_added(self, collector, book):
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_added(self, collector):
        book = 'Шестой элемент'
        genre = 'Фантастика'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre_displayed_book(self, collector_len_five):

        assert collector_len_five.get_books_with_specific_genre('Детективы') == ['Остров проклятых']

    def test_get_books_for_children_displayed_list(self, collector_len_five):
        books_for_children = collector_len_five.get_books_for_children()

        assert len(books_for_children) == 3 and books_for_children == ['Футурама', 'Евротур', 'Шестой элемент']

    def test_add_book_in_favorites_is_added(self, collector):
        book = 'Шестой элемент'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()

        assert len(favorites) == 1 and favorites[0] == book

    def test_add_book_in_favorites_is_not_added(self, collector):
        book = 'Шестой элемент'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()

        assert len(favorites) == 1 and favorites[0] == book

    def test_delete_book_from_favorites_deleted_book(self, collector):
        book = 'Шестой элемент'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_not_deleted_book(self, collector):
        book = 'Шестой элемент'
        book2 = 'Футурама'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book2)
        favorites = collector.get_list_of_favorites_books()

        assert len(favorites) == 1 and favorites[0] == book
