from flet import Dropdown, TextStyle, colors, dropdown


dropdown_transportistas = Dropdown(
        label="Transportista",
        hint_text="Selecciona una opción",
        label_style=TextStyle(color=colors.LIGHT_BLUE_400),
        # autofocus=True,
        border_width=0.7,
        border_color=colors.LIGHT_BLUE_400,
        options=[
            dropdown.Option("Transportista 1"),
            dropdown.Option("Transportista 2"),
            dropdown.Option("Transportista 3")
        ]
    )
