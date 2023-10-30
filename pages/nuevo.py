import flet as ft
import requests
import json


URL = "https://mrjuw5qxmbxnnsdljvsqfoyv640yondi.lambda-url.us-east-2.on.aws"


razon_social = ft.TextField(
    label="Razón social",
    hint_text="Agrega un valor",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400
)

correos = ft.TextField(
    label="Correos",
    hint_text="Agrega los correos del transportista",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400,
    multiline=True,
    max_lines=9,
    height=250
)


def _view_():
    def create_sociedad(e):
        if razon_social.value != "" and correos.value != "":
            try:
                sociedad = {
                    "nombre": razon_social.value,
                    "correos": correos.value
                }
                sociedad = json.dumps(sociedad)

                response = requests.post(
                    url=f"{URL}/sociedades",
                    data=sociedad
                )

                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        value="Nueva razón social agregada",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    bgcolor=ft.colors.LIGHT_BLUE_200
                )
                e.page.snack_bar.duration = 3000
                e.page.snack_bar.open = True

                razon_social.value = ""
                correos.value = ""
                e.page.update()

            except:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Error al insertar a base de datos", text_align=ft.TextAlign.CENTER),
                    bgcolor="red"
                )
                e.page.snack_bar.duration = 3000
                e.page.snack_bar.open = True
                e.page.update()
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("Todos los campos son obligatorios", text_align=ft.TextAlign.CENTER, size=18),
                bgcolor="#ff6347"
            )
            e.page.snack_bar.duration = 3000
            e.page.snack_bar.open = True
            e.page.update()



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
            razon_social,
            correos,
            ft.Container(
                content=ft.ElevatedButton(
                    text="Agregar",
                    icon="ADD_CIRCLE_ROUNDED",
                    on_click=create_sociedad
                ),
                height=150,
                alignment=ft.alignment.bottom_right,
            )
        ]
    )
