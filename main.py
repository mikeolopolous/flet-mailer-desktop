import flet as ft


from pages.index import _view_ as index_view
from pages.nuevo import _view_ as nuevo_view
from pages.editar import _view_ as editar_view
from pages.eliminar import _view_ as eliminar_view


def main(page: ft.Page):
    page.title = "Mailer App"
    page.window_width = 500
    page.window_height = 600

    index = index_view()
    nuevo = nuevo_view()
    editar = editar_view()
    eliminar = eliminar_view()


    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(index)
        page.update()

        if page.route == "/nuevo":
            page.views.append(nuevo)
        page.update()

        if page.route == "/editar":
            page.views.append(editar)
        page.update()

        if page.route == "/eliminar":
            page.views.append(eliminar)
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
