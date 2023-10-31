import flet as ft
import requests


URL = "https://mrjuw5qxmbxnnsdljvsqfoyv640yondi.lambda-url.us-east-2.on.aws"

razon_social = ft.TextField(
    label="Razón social",
    hint_text="Buscar transportista",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400,
    width=420
)

correos = ft.TextField(
    label="Correos",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400,
    multiline=True,
    max_lines=9,
    height=250,
    disabled=True
)

id_razon_social = ""


def _view_():
    def search_razon_social(e):
        global id_razon_social
        nombre = razon_social.value
        response = requests.get(f"{URL}/sociedades/{nombre}")

        if response.status_code == 200:
            data = response.json()
            id_razon_social = data["id"]
            correos.value = data["correos"]
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("No se encontró la razón social", text_align=ft.TextAlign.CENTER),
                bgcolor="#ff6347"
            )
            e.page.snack_bar.duration = 3000
            e.page.snack_bar.open = True
        
        e.page.update()

    
    def delete_razon_social(e):
        if razon_social.value != "" and id_razon_social != "":
            try:
                response = requests.delete(f"{URL}/sociedades/{id_razon_social}")

                if response.status_code == 204:
                    e.page.snack_bar = ft.SnackBar(
                        content=ft.Text(
                            value="Razón social eliminada",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        bgcolor=ft.colors.LIGHT_BLUE_200
                    )
                    e.page.snack_bar.duration = 3000
                    e.page.snack_bar.open = True

                    razon_social.value = ""
                    correos.value = ""

                if response.status_code == 404:
                    e.page.snack_bar = ft.SnackBar(
                        content=ft.Text(
                            value="No existe la razón social",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        bgcolor="#ff6347"
                    )
                    e.page.snack_bar.duration = 3000
                    e.page.snack_bar.open = True

                e.page.update()
            except:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Error al insertar a base de datos", text_align=ft.TextAlign.CENTER),
                    bgcolor="#ff6347"
                )
                e.page.snack_bar.duration = 3000
                e.page.snack_bar.open = True
                e.page.update()
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("El campo de razón social está vacío", text_align=ft.TextAlign.CENTER),
                bgcolor="#ff6347"
            )
            e.page.snack_bar.duration = 3000
            e.page.snack_bar.open = True
            e.page.update()


    row_search_razon_social = ft.Row(
        controls=[
            razon_social,
            ft.IconButton(
                icon="SEARCH",
                icon_size=40,
                icon_color=ft.colors.LIGHT_BLUE_400,
                on_click=search_razon_social
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
            row_search_razon_social,
            correos,
            ft.Container(
                content=ft.ElevatedButton(
                    text="Eliminar",
                    icon="DELETE",
                    on_click=delete_razon_social
                ),
                height=150,
                alignment=ft.alignment.bottom_right
            ),
        ]
    )