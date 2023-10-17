import flet as ft


container_send_email = ft.Container(
    content=ft.ElevatedButton(
        text="Enviar email",
        icon="send_rounded"
    ),
    height=150,
    alignment=ft.alignment.bottom_right
)