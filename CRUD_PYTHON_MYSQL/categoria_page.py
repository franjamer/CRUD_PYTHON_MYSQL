import reflex as rx
from .models.categoria_model import Categoria
from .services.categoria_service import select_all_categoria_service


class CategoriaState(rx.State):
    categoriastabla: list[Categoria]=[{"nombrecategoria":"Juntas","departamento":"mecanico"},{"nombrecategoria":"reductores","departamento":"mecanico"}]
    

    @rx.event(background=True)
    async def get_all_categoria(self):
        async with self:
            self.categoriastabla = select_all_categoria_service()


@rx.page(route='/categorias', title='categorias', on_load=CategoriaState.get_all_categoria)
def categoria_page() -> rx.Component:
    return rx.flex(
        rx.heading("Categorias", align='center'),

        table_categoria(CategoriaState.categoriastabla),
        direction='column',
        style={'width': '50vw', 'margin': 'auto', 'background_color': 'gray'}
    )


def table_categoria(list_categoria: list[Categoria]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre de Categoria"),
                rx.table.column_header_cell("Departamento")
            )
        ),
        rx.table.body(
            rx.foreach(list_categoria, row_table_categoria,  # Usa row_table para evitar duplicar lógica
                       ),

        )
    )


def row_table_categoria(categoria: Categoria) -> rx.Component:
    return rx.table.row(
        rx.table.cell(categoria.nombrecategoria),
        rx.table.cell(categoria.departamento),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar"),
        )
        )
    )
