import flet as ft


def _view_():

    return ft.View(
        "/nuevo",
        controls=[
            ft.Text(value="Hola nuevo transportista"),
            ft.ElevatedButton("Inicio", on_click=lambda e: e.page.go("/"))
        ]
    )
