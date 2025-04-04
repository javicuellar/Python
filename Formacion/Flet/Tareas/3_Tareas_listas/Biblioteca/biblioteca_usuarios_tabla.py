import flet as ft



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Author:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name):
        self.name = name

def main(page: ft.Page):
    books = [
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]

    authors = [
        Author("George Orwell"),
        Author("Harper Lee"),
        Author("F. Scott Fitzgerald")
    ]

    users = [
        User("Alice"),
        User("Bob"),
        User("Charlie")
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

    def update_author(e):
        index = int(e.control.data)
        authors[index].name = author_name_input.value
        page.update()

    def delete_author(e):
        index = int(e.control.data)
        authors.pop(index)
        page.update()

    def edit_author(e):
        index = int(e.control.data)
        author_name_input.value = authors[index].name
        page.update()

    def update_user(e):
        index = int(e.control.data)
        users[index].name = user_name_input.value
        page.update()

    def delete_user(e):
        index = int(e.control.data)
        users.pop(index)
        page.update()

    def edit_user(e):
        index = int(e.control.data)
        user_name_input.value = users[index].name
        page.update()

    title_input = ft.TextField(label="Title")
    author_input = ft.TextField(label="Author")
    author_name_input = ft.TextField(label="Author Name")
    user_name_input = ft.TextField(label="User Name")

    def create_table(data, headers, edit_callback, delete_callback):
        table = ft.DataTable(
            show_checkbox_column=True,
            columns=[ft.DataColumn(ft.Text(header)) for header in headers],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(getattr(item, attr))) for attr in headers
                    ] + [
                        ft.DataCell(ft.FilledTonalButton(text="Edit", data=i, on_click=edit_callback)),
                        ft.DataCell(ft.FilledTonalButton(text="Delete", data=i, on_click=delete_callback))
                    ]
                ) for i, item in enumerate(data)
            ]
        )
        return table

    def show_books(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Library Management - Books"),
                    title_input,
                    author_input,
                    ft.FilledTonalButton(text="Update Book", on_click=update_book),
                    create_table(books, ["title", "author"], edit_book, delete_book)
                ]
            )
        )
        page.update()

    def show_authors(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Library Management - Authors"),
                    author_name_input,
                    ft.FilledTonalButton(text="Update Author", on_click=update_author),
                    create_table(authors, ["name"], edit_author, delete_author)
                ]
            )
        )
        page.update()

    def show_users(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Library Management - Users"),
                    user_name_input,
                    ft.FilledTonalButton(text="Update User", on_click=update_user),
                    create_table(users, ["name"], edit_user, delete_user)
                ]
            )
        )
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.FilledTonalButton(text="Books", on_click=show_books),
                        ft.FilledTonalButton(text="Authors", on_click=show_authors),
                        ft.FilledTonalButton(text="Users", on_click=show_users)
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        ft.Text("Select an option from the menu")
                    ]
                )
            ]
        )
    )

ft.app(target=main)