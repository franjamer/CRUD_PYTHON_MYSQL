"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .user_page import user_page
from .categoria_page import categoria_page

class State(rx.State):
    """The app state."""

    ...


"""Página de inicio (Index) con enlaces a las otras páginas."""
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.button(
                rx.link(
                    "Usuarios",
                    href="/usuarios"  # Corrige href para usar la ruta.
                )
            ),
            rx.button(
                rx.link(
                    "Categorías",
                    href="/categorias"  # Corrige href para usar la ruta.
                )
            ),
            spacing="1",  # Ajusta el espaciado entre botones si es necesario.
        ),
        padding="2rem",  # Opcional: agrega padding al contenedor.
    )

    


app = rx.App()
app.add_page(index, route="/")
app.add_page(user_page,route="/usuarios")
app.add_page(categoria_page,route="/categorias")