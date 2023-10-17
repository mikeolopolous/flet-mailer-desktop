import flet as ft


from widgets.dropdown_transportista import dropdown_transportistas
from widgets.container_send_button import container_send_email


def _view_():

    container_correos_transportista = ft.Container(
        # content=, Acá va la lista de correos
        height=250,
        bgcolor="gray",
        border=ft.border.all(width=0.7, color=ft.colors.LIGHT_BLUE_400)
    )


    return ft.View(
        route="/",
        appbar=ft.AppBar(
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
        ),
        controls=[dropdown_transportistas, container_correos_transportista, container_send_email]
    )
