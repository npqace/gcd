def input_book():
    book_name = input("Nhập tên cuốn sách: ")
    book_author = input("Nhập tên tác giả: ")
    quantity = int(input("Nhập số lượng sách: "))
    return {'book_name' : book_name, 'book_author' : book_author, 'quantity' : quantity}

def print_book(book):
    print(f"Tên sách: {book['book_name']}")
    print(f"Tên tác giả: {book['book_author']}")
    print(f"Số lượng: {book['quantity']}")

library = []
n = int(input("Nhập số lượng sách (tối đa 10 cuốn): "))
print("Xin mời nhập thông tin cho các cuốn sách.")
for i in range(n):
    print(f"Nhập thông tin cho cuốn sách {i+1}:")
    book_info = input_book()
    library.append(book_info)
    if i == 9:
        print("Đã đạt số lượng sách tối đa!")
        break

print()
print("----------")
print()

# tìm sách theo tên
def find_book_by_name(library, book_name):
    book_by_name = []
    for book in library:
        if book['book_name'] == book_name:
            book_by_name.append(book)
    return book_by_name

find_book_name = input("Nhập tên sách bạn muốn tìm: ")
book_by_name = find_book_by_name(library, find_book_name)
if book_by_name:
    print("Thông tin của cuốn sách: ")
    for book in book_by_name:
        print_book(book)
else:
    print("Book not found!")

print()
print("----------")
print()

# tổng số sách trong thư viện
def count_total(library):
    total = 0
    for book in library:
        total += book['quantity']
    return total

print(f"Tổng số sách trong thư viện: {count_total(library)}")

print()
print("----------")
print()

# tìm sách có cùng tên tác giả
def find_book_by_author(library, book_author):
    book_by_author = []
    for book in library:
        if book['book_author'] == book_author:
            book_by_author.append(book['book_name'])
    return book_by_author

def author_book(book):
    return f"{book['book-author']}"

find_book_author = input("Nhập tên tác giả sách bạn muốn tìm: ")
book_by_author = find_book_by_author(library, find_book_author)
author_book = ', '.join(book_by_author)

if book_by_author:
    print(f"Sách của tác giả {find_book_author}: {author_book}")