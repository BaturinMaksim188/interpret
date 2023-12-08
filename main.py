import flet as ft
import pyautogui

from database.database import UserBook, User
from tools.books import pick_files_result


def main(page: ft.Page):
    width, height = pyautogui.size()
    page.window_width = 2400 #width * 0.75
    page.window_height = 1080 #height * 0.75
    page.padding = height * 0.05
    page.title = "Interpret"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # main_user = User.select().where()
    page.update()

    def get_page(e, index=None):
        if index is None:
            index = e.control.selected_index
        if index == 0:
            tab_1.controls[0] = ft.Container(ft.ResponsiveRow([
                set_user_books(),
            ]))
            tab_1.visible = True
        else:
            tab_1.visible = False
        tab_2.visible = True if index == 1 else False
        tab_3.visible = True if index == 2 else False
        tab_4.visible = True if index == 3 else False
        page.update()

    def set_user_books():
        books = ft.ResponsiveRow([ft.Container(ft.ElevatedButton(
            content=ft.Row([
                ft.Text(f"{book.name}",
                        max_lines=2,
                        expand=True,
                        overflow=ft.TextOverflow.ELLIPSIS),
                ft.Icon(name=ft.icons.FILE_DOWNLOAD_DONE_SHARP, color="black", ),
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=page.window_height * 0.07,
            )),
            margin=ft.margin.only(bottom=page.window_height * 0.01)
        ) for book in UserBook.select().where(UserBook.format == 'txt')], )

        if len(books.controls) > 0:
            return books
        else:
            return ft.Container(
                content=ft.Text(f"Добавьте книгу в форматах: \".txt\", \".txt\", \".txt\", \".txt\".",
                                max_lines=10,
                                text_align=ft.TextAlign.CENTER,
                                expand=True,
                                overflow=ft.TextOverflow.NONE,
                                ),
                alignment=ft.alignment.center,
                height=page.window_height * 0.12,
                bgcolor='#b1bdfc',
                border_radius=30,
                padding=ft.padding.only(left=page.window_width * 0.02, right=page.window_width * 0.02),
                margin=ft.margin.only(bottom=page.window_height * 0.02)

            )

    def get_userbook(e):
        pick_files_dialog.pick_files(
            allow_multiple=False
        )

    def pick_files_result_and_update(e: ft.FilePickerResultEvent):
        pick_files_result(e)
        get_page(e, index=0)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_SHARP, label="Главная"),
            ft.NavigationDestination(icon=ft.icons.CLOUD_QUEUE, selected_icon=ft.icons.CLOUD, label="Книги"),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Уроки"),
            ft.NavigationDestination(icon=ft.icons.VIEW_LIST_OUTLINED, selected_icon=ft.icons.VIEW_LIST,
                                     label="Прочее"),

        ],
        selected_index=0,
        elevation=1,
        bgcolor='#9da6f2',
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_HIDE,
        on_change=get_page,
        height=page.window_height * 0.10,
    )

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result_and_update)
    page.overlay.append(pick_files_dialog)

    tab_1 = ft.ResponsiveRow(
        [
            set_user_books(),
            ft.FilledTonalButton("Добавить книгу", icon=ft.icons.UPLOAD_OUTLINED, height=page.window_height * 0.05,
                                 visible=True,
                                 on_click=get_userbook,
                                 ),
        ]
    )

    # tab_1 = ft.Text("Tab 1", size=30, visible=True)
    tab_2 = ft.Text(f"{page.window_width, page.window_height}", size=30, visible=False)
    tab_3 = ft.Text("Tab 3", size=30, visible=False)
    tab_4 = ft.Text("Tab 4", size=30, visible=False)

    page.add(
        tab_1,
        tab_2,
        tab_3,
        tab_4
    )


ft.app(target=main)
