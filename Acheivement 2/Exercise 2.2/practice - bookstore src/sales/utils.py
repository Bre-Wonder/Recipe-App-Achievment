from books.models import Book
# connect parameters from books model


def get_bookname_from_id(val):
    bookname = Book.objects.get(id=val)
    return bookname
