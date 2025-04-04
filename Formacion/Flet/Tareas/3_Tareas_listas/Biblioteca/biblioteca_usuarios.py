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

    book_list = ft.Column()
    author_list = ft.Column()
    user_list = ft.Column()

    for i, book in enumerate(books):
        book_list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(book.title),
                    ft.Text(book.author),
                    ft.FilledTonalButton(text="Edit", data=i, on_click=edit_book),
                    ft.FilledTonalButton(text="Delete", data=i, on_click=delete_book)
                ]
            )
        )

    for i, author in enumerate(authors):
        author_list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(author.name),
                    ft.FilledTonalButton(text="Edit", data=i, on_click=edit_author),
                    ft.FilledTonalButton(text="Delete", data=i, on_click=delete_author)
                ]
            )
        )

    for i, user in enumerate(users):
        user_list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(user.name),
                    ft.FilledTonalButton(text="Edit", data=i, on_click=edit_user),
                    ft.FilledTonalButton(text="Delete", data=i, on_click=delete_user)
                ]
            )
        )

    def show_books(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Library Management - Books"),
                    title_input,
                    author_input,
                    ft.FilledTonalButton(text="Update Book", on_click=update_book),
                    book_list
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
                    author_list
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
                    user_list
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