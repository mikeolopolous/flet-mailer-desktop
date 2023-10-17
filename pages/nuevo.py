import flet as ft


from widgets.container_add_button import container_add_transportista


def _view_():

    return ft.View(
        "/nuevo",
        appbar=ft.AppBar(
            title=ft.Text(value="Agregar transportista", color=ft.colors.LIGHT_BLUE_400),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(icon=ft.icons.WB_SUNNY, icon_color=ft.colors.AMBER_300),
                ft.PopupMenuButton(
                    icon=ft.icons.MENU,
                    items=[
                        ft.PopupMenuItem(text="Enviar", on_click=lambda e: e.page.go("/")),
                        ft.PopupMenuItem(text="Editar", on_click=lambda e: e.page.go("/editar")),
                        ft.PopupMenuItem(text="Eliminar", on_click=lambda e: e.page.go("/eliminar"))
                    ]

                )
            ]
        ),
        controls=[
            ft.TextField(
                label="Razón social",
                hint_text="Agrega un valor",
                label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
                border_width=0.7,
                border_color=ft.colors.LIGHT_BLUE_400
            ),
            ft.TextField(
                label="Correos",
                hint_text="Agrega los correos del transportista",
                label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
                border_width=0.7,
                border_color=ft.colors.LIGHT_BLUE_400,
                multiline=True,
                max_lines=9,
                height=250
            ),
            container_add_transportista
        ]
    )
