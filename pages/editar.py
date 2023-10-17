import flet as ft


def _view_():

    return ft.View(
        "/editar",
        controls=[
            ft.Text(value="Editar transportista"),
            ft.ElevatedButton("Inicio", on_click=lambda e: e.page.go("/"))
        ]
    )