import flet as ft

def main(page: ft.Page):
    page.title = "Mailer App"
    page.window_width = 500

    lbl_transportista = ft.Text(value="Transportista:", size=30)

    dd_transportista = ft.Dropdown(
        label="Transportista",
        hint_text="Selecciona una opción",
        autofocus=True,
        border_width=0.7,
        options=[
            ft.dropdown.Option("Transportista 1"),
            ft.dropdown.Option("Transportista 2"),
            ft.dropdown.Option("Transportista 3")
        ]
    )

    lbl_correos_transportista = ft.Text(value="Destinatarios:", size=30)

    container_correos_transportista = ft.Container(
        # content=[], Acá va la lista de correos
        height=250,
        bgcolor="gray",
        border=ft.border.all(width=0.7, color=ft.colors.INDIGO_400)
    )

    btn_enviar_email = ft.ElevatedButton(text="Enviar email", icon="send_rounded")

    page.add(
        lbl_transportista,
        dd_transportista,
        lbl_correos_transportista,
        container_correos_transportista,
        btn_enviar_email
    )


ft.app(target=main)
