import flet as ft


from widgets.navbar import navbar
from widgets.dropdown_transportista import menu_navbar


def main(page: ft.Page):
    page.title = "Mailer App"
    page.window_width = 500
    page.window_height = 650
    # page.theme_mode = "LIGHT"

    page.appbar = navbar

    dd_transportista = menu_navbar

    lbl_correos_transportista = ft.Text(value="Destinatarios:", size=30)

    container_correos_transportista = ft.Container(
        # content=, Acá va la lista de correos
        height=250,
        bgcolor="gray",
        border=ft.border.all(width=0.7, color=ft.colors.LIGHT_BLUE_400)
    )

    btn_enviar_email = ft.ElevatedButton( #needs fix the style :|
        text="Enviar email",
        icon="send_rounded",
        color=ft.colors.BLACK87,
        bgcolor=ft.colors.LIGHT_BLUE_300
    )

    container_send_email_button = ft.Container(
        content=btn_enviar_email,
        height=150,
        alignment=ft.alignment.bottom_right
    )

    page.add(
        dd_transportista,
        lbl_correos_transportista,
        container_correos_transportista,
        container_send_email_button
    )


ft.app(target=main)
