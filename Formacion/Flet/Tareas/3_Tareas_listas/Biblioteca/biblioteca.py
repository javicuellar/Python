import flet as ft



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def main(page: ft.Page):
    books = [
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]

    def update_book(e):
        index = int(e.control.data)
        books[index].title = title_input.value
        books[index].author = author_input.value
        page.update()

    def delete_book(e):
        index = int(e.control.data)
        books.pop(index)
        page.update()

    def edit_book(e):
        index = int(e.control.data)
        title_input.value = books[index].title
        author_input.value = books[index].author
        page.update()

    title_input = ft.TextField(label="Title")
    author_input = ft.TextField(label="Author")

    book_list = ft.Column()

    for i, book in enumerate(books):
        book_list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(book.title),
                    ft.Text(book.author),
                    ft.ElevatedButton(text="Edit", data=i, on_click=edit_book),
                    ft.ElevatedButton(text="Delete", data=i, on_click=delete_book)
                ]
            )
        )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Library Management"),
                title_input,
                author_input,
                ft.ElevatedButton(text="Update Book", on_click=update_book),
                book_list
            ]
        )
    )

ft.app(target=main)