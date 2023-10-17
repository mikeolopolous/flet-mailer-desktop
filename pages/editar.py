import flet as ft


from widgets.container_edit_button import container_edit_button


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
        "/editar",
        appbar=ft.AppBar(
            title=ft.Text(value="Editar transportista", color=ft.colors.LIGHT_BLUE_400),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(icon=ft.icons.WB_SUNNY, icon_color=ft.colors.AMBER_300),
                ft.PopupMenuButton(
                    icon=ft.icons.MENU,
                    items=[
                        ft.PopupMenuItem(text="Enviar", on_click=lambda e: e.page.go("/")),
                        ft.PopupMenuItem(text="Nuevo", on_click=lambda e: e.page.go("/nuevo")),
                        ft.PopupMenuItem(text="Eliminar", on_click=lambda e: e.page.go("/eliminar"))
                    ]

                )
            ]
        ),
        controls=[
            row_search_transportista,
            ft.TextField(
                label="Nueva razón social",
                hint_text="vieja razón social", # Acá va la antigua razón social como guía
                label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
                border_width=0.7,
                border_color=ft.colors.LIGHT_BLUE_400
            ),
            ft.TextField(
                label="Correos",
                hint_text="correos actuales", # Acá va la lista de correos actuales
                label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
                border_width=0.7,
                border_color=ft.colors.LIGHT_BLUE_400,
                multiline=True,
                max_lines=9,
                height=250
            ),
            container_edit_button
        ]
    )
