import flet as ft


def add_book():
    pass


def add_book_to_list():
    pass


def pick_files_result(e: ft.FilePickerResultEvent):
    print(e.files[0].name)
