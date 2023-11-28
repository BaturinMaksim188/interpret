import time

import flet as ft
from flet_core import NavigationBarLabelBehavior


def main(page: ft.Page):
    page.window_width = 460
    page.window_height = 780
    page.title = "NavigationBar Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    def get_page(e):
        index = e.control.selected_index
        tab_1.visible = True if index == 0 else False
        tab_2.visible = True if index == 1 else False
        tab_3.visible = True if index == 2 else False
        tab_4.visible = True if index == 3 else False
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_SHARP, label="Главная"),
            ft.NavigationDestination(icon=ft.icons.CLOUD_QUEUE, selected_icon=ft.icons.CLOUD, label="Книги"),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Уроки"),
            ft.NavigationDestination(icon=ft.icons.VIEW_LIST_OUTLINED, selected_icon=ft.icons.VIEW_LIST, label="Прочее"),

        ],
        selected_index=0,
        elevation=1,
        bgcolor='#9da6f2',
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_HIDE,
        on_change=get_page,
        height=page.window_height / 12,
    )

    tab_1 = ft.Text("Tab 1", size=30, visible=True)
    tab_2 = ft.Text("Tab 2", size=30, visible=False)
    tab_3 = ft.Text("Tab 3", size=30, visible=False)
    tab_4 = ft.Text("Tab 4", size=30, visible=False)

    page.add(
        ft.Container(
            content=ft.Column([
                tab_1,
                tab_2,
                tab_3,
                tab_4
            ])
        )
    )


ft.app(target=main)
