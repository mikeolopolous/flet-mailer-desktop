import flet as ft


from widgets.dropdown_transportista import dropdown_transportistas


def _view_():

    navbar = ft.AppBar(
        title=ft.Text(value="Enviar correo", color=ft.colors.LIGHT_BLUE_400),
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(icon=ft.icons.WB_SUNNY, icon_color=ft.colors.AMBER_300),
            ft.PopupMenuButton(
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(text="Nuevo", on_click=lambda e: e.page.go(route="/nuevo")),
                    ft.PopupMenuItem(text="Editar", on_click=lambda e: e.page.go(route="/editar")),
                    ft.PopupMenuItem(text="Eliminar", on_click=lambda e: e.page.go(route="/eliminar")),
                ]
            )
        ]
    )

    return ft.View(
        route="/",
        appbar=navbar,
        controls=[dropdown_transportistas]
    )