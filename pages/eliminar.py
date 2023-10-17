import flet as ft


def _view_():

    return ft.View(
        "/eliminar",
        controls=[
            ft.Text(value="Eliminar transportista"),
            ft.ElevatedButton("Inicio", on_click=lambda e: e.page.go("/"))
        ]
    )