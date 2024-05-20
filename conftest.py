import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def collector_len_five(collector):
    collection = collector
    books = ['Футурама', 'ОНО', 'Евротур', 'Остров проклятых', 'Шестой элемент']
    genres = ['Мультфильмы', 'Ужасы', 'Комедии', 'Детективы', 'Фантастика']
    for i in range(5):
        collection.add_new_book(books[i])

    for i in range(5):
        collection.set_book_genre(books[i], genres[i])

    return collection
