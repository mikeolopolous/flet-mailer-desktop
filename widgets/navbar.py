from flet import AppBar, Text, colors, IconButton, icons, PopupMenuButton, PopupMenuItem


navbar = AppBar(
        title=Text(value="Enviar correo", color=colors.LIGHT_BLUE_400),
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icon=icons.WB_SUNNY, icon_color=colors.AMBER_300),
            PopupMenuButton(
                icon=icons.MENU,
                items=[
                    PopupMenuItem(text="View 2"),
                    PopupMenuItem(text="View 3"),
                    PopupMenuItem(text="View 4"),
                ]
            )
        ]
    )