import flet as ft


from widgets.dropdown_transportista import dropdown_transportistas


def main(page: ft.Page):
    page.title = "Mailer App"
    page.window_width = 500
    page.window_height = 650

    navbar = ft.AppBar(
        title=ft.Text(value="Enviar correo", color=ft.colors.LIGHT_BLUE_400),
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(icon=ft.icons.WB_SUNNY, icon_color=ft.colors.AMBER_300),
            ft.PopupMenuButton(
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(text="Nuevo", on_click=lambda _: page.go(route="/nuevo")),
                    ft.PopupMenuItem(text="Editar", on_click=lambda _: page.go(route="/editar")),
                    ft.PopupMenuItem(text="Eliminar", on_click=lambda _: page.go(route="/eliminar")),
                ]
            )
        ]
    )

    container_correos_transportista = ft.Container(
        # content=, Acá va la lista de correos
        height=250,
        bgcolor="gray",
        border=ft.border.all(width=0.7, color=ft.colors.LIGHT_BLUE_400)
    )

    container_send_email = ft.Container(
        content=ft.ElevatedButton(
            text="Enviar email",
            icon="send_rounded"
        ),
        height=150,
        alignment=ft.alignment.bottom_right
    )

    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    navbar,
                    dropdown_transportistas,
                    ft.Text(value="Destinatarios:", size=30),
                    container_correos_transportista,
                    container_send_email
                ],
            )
        )

        if page.route == "/nuevo":
            page.views.append(
                ft.View(
                    "/nuevo",
                    [
                        ft.Text(value="Hola nuevo transportista"),
                        ft.ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                    ]
                )
            )

        if page.route == "/editar":
            page.views.append(
                ft.View(
                    "/editar",
                    [
                        ft.Text(value="Editar transportista"),
                        ft.ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                    ]
                )
            )

        if page.route == "/eliminar":
            page.views.append(
                ft.View(
                    "/eliminar",
                    [
                        ft.Text(value="Eliminar transportista"),
                        ft.ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                    ]
                )
            )
        
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
