import flet as ft


from widgets.container_delete_button import container_delete_button


def _view_():

    row_search_transportista = ft.Row(
        controls=[
            ft.TextField(
                label="Razón social",
                hint_text="Buscar transportista",
                label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
                border_width=0.7,
                border_color=ft.colors.LIGHT_BLUE_400,
                width=420
            ),
            ft.IconButton(
                icon="SEARCH",
                icon_size=40,
                icon_color=ft.colors.LIGHT_BLUE_400
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    return ft.View(
        "/eliminar",
        appbar=ft.AppBar(
            title=ft.Text(value="Eliminar transportista", color=ft.colors.LIGHT_BLUE_400),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(icon=ft.icons.WB_SUNNY, icon_color=ft.colors.AMBER_300),
                ft.PopupMenuButton(
                    icon=ft.icons.MENU,
                    items=[
                        ft.PopupMenuItem(text="Enviar", on_click=lambda e: e.page.go("/")),
                        ft.PopupMenuItem(text="Nuevo", on_click=lambda e: e.page.go("/nuevo")),
                        ft.PopupMenuItem(text="Editar", on_click=lambda e: e.page.go("/editar"))
                    ]

                )
            ]
        ),
        controls=[
            row_search_transportista,
            container_delete_button
        ]
    )