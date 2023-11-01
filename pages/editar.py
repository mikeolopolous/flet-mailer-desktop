import flet as ft
import requests
import json


old_sociedad = ft.TextField(
    label="Razón social",
    hint_text="Buscar transportista",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400,
    width=420
)

updated_sociedad = ft.TextField(
    label="Nueva razón social",
    hint_text="Ingresa un nombre",
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400
)

updated_correos = ft.TextField(
    label="Correos",
    hint_text='Correos separados por ";"',
    label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_400),
    border_width=0.7,
    border_color=ft.colors.LIGHT_BLUE_400,
    multiline=True,
    max_lines=9,
    height=250
)


URL = "https://mrjuw5qxmbxnnsdljvsqfoyv640yondi.lambda-url.us-east-2.on.aws"
dict_sociedad = {
    "id": "",
    "nombre": "",
    "correos": ""
}


def _view_():
    def search_razon_social(e):
        global dict_sociedad
        sociedad = old_sociedad.value

        if sociedad != "":
            try:
                response = requests.get(f"{URL}/sociedades/{sociedad}")
                data = response.json()

                if response.status_code == 200:
                    dict_sociedad["id"] = data["id"]

                    updated_sociedad.value = data["nombre"]
                    updated_correos.value = data["correos"]

            except:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("No se encontró la razón social", text_align=ft.TextAlign.CENTER),
                    bgcolor="#ff6347"
                )
                e.page.snack_bar.duration = 3000
                e.page.snack_bar.open = True
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("El campo razón social está vacío", text_align=ft.TextAlign.CENTER),
                bgcolor="#ff6347"
            )
            e.page.snack_bar.duration = 3000
            e.page.snack_bar.open = True

        e.page.update()


    def update_sociedad(e):
        global dict_sociedad

        if dict_sociedad["id"] != "" and updated_sociedad.value != "" and updated_correos.value != "":
            dict_sociedad["nombre"] = updated_sociedad.value
            dict_sociedad["correos"] = updated_correos.value
            
            json_sociedad = json.dumps(dict_sociedad)

            try:
                response = requests.put(f"{URL}/sociedades", data=json_sociedad)

                if response.status_code == 200:
                    e.page.snack_bar = ft.SnackBar(
                        content=ft.Text("Razón social modificada correctamente", text_align=ft.TextAlign.CENTER),
                        bgcolor=ft.colors.LIGHT_BLUE_200
                    )
                    e.page.snack_bar.duration = 3000
                    e.page.snack_bar.open = True

                    old_sociedad.value = ""
                    updated_sociedad.value = ""
                    updated_correos.value = ""
                    dict_sociedad = {
                        "id": "",
                        "nombre": "",
                        "correos": ""
                    }

            except:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Error al modificar base de datos", text_align=ft.TextAlign.CENTER),
                    bgcolor="#ff6347"
                )
                e.page.snack_bar.duration = 3000
                e.page.snack_bar.open = True

        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("Todos los campos son obligatorios", text_align=ft.TextAlign.CENTER),
                bgcolor="#ff6347"
            )
            e.page.snack_bar.duration = 3000
            e.page.snack_bar.open = True
        
        e.page.update()

    row_search_sociedad = ft.Row(
        controls=[
            old_sociedad,
            ft.IconButton(
                icon="SEARCH",
                icon_size=40,
                icon_color=ft.colors.LIGHT_BLUE_400,
                on_click=search_razon_social
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    container_edit_button = ft.Container(
        content=ft.ElevatedButton(
            text="Editar",
            icon="EDIT",
            on_click=update_sociedad
        ),
        height=85,
        alignment=ft.alignment.bottom_right
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
            row_search_sociedad,
            updated_sociedad,
            updated_correos,
            container_edit_button
        ]
    )
