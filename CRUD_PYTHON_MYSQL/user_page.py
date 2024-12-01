import reflex as rx
from .models.user_model import User
from .services.user_service import select_all_user_service, select_user_by_email_service, create_user_service, delete_user_service
from .notify import notify_component
import asyncio


""" PAGINA DE USUARIOS """
# Apartir de aqui es la pagina de usuarios

# Mantiene los usuarios como diccionarios para evitar problemas.


class UserState(rx.State):
    users: list[User]
    # [{"name":"Jose","username":"JMM","phone":"99884488"},{
    #      "name":"Paco","username":"fjmr","phone":"99988745"},{
    #          "name":"Pepe","username":"Pepe","phone":"9333345"
    #      }]
    user_buscar: str
    error_message: str
    error: str = ''

    @rx.event(background=True)
    async def create_user(self, data: dict):
        async with self:
            print("Datos Recibidos:", data)
            try:
                self.users = create_user_service(
                    username=data['username'], password=data['password'], phone=data['phone'], name=data['name'])
            except BaseException as be:
                print(be.args)
                self.error_message = str(be)
                self.error = be.args[0] if be.args else 'Error Desconocido'
        await self.handleNotify()

    @rx.event(background=True)
    # @rx.background #se quedó obsoleto
    async def get_all_user(self):
        # Obtén usuarios y conviértelos a diccionarios
        async with self:
            self.users = [user for user in select_all_user_service()]

    @rx.event(background=True)
    async def get_user_by_email(self):
        async with self:
            self.users = select_user_by_email_service(self.user_buscar)

    # maneja la notificación en forma de pop-up cuando hay un error
    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error = ''

    def buscar_on_change(self, value: str):
        self.user_buscar = value

    @rx.event(background=True)
    async def delete_user_by_email(self, email):
        async with self:
            self.users = delete_user_service(email)


@rx.page(route='/user', title='users', on_load=UserState.get_all_user)
def user_page() -> rx.Component:
    return rx.flex(
        rx.heading("Usuarios", align='center'),
        rx.hstack(
            buscar_user_component(),
            create_user_dialogo_component(),
            justify="center",
            style={'margin-top': '30px'}
        ),
        table_use(UserState.users),
        rx.cond(
            UserState.error != '',
            notify_component(UserState.error, 'shield-alert', 'yellow')
        ),
        direction='column',
        style={'width': '50vw', 'margin': 'auto', 'background_color': 'gray'}
    )



def table_use(list_user: list[User]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Telefono"),
                rx.table.column_header_cell("Accion"),
            )
        ),
        rx.table.body(
            rx.foreach(list_user, row_table,  # Usa row_table para evitar duplicar lógica
                       ),

        )
    )


def row_table(user: User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.username),
        rx.table.cell(user.phone),
        rx.table.cell(rx.hstack(
            delete_user_dialogo_component(user.username),
        )
        )
    )


def buscar_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ingrese email",
                 on_change=UserState.buscar_on_change),
        rx.button("Buscar Usuario", on_click=UserState.get_user_by_email)
    )


def create_user_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Nombre",
                name="name"
            ),
            rx.input(
                placeholder="Email",
                name="username"
            ),
            rx.input(
                placeholder="Contraseña",
                name="password",
                type="password"
            ),
            rx.input(
                placeholder="Teléfono",
                name="phone"
            ),
            rx.dialog.close(
                rx.button('Guardar', type='submit')
            )
        ),
        on_submit=UserState.create_user,
    )


def create_user_dialogo_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Crear Usuario")),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear Usuario"),
                create_user_form(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.text(UserState.error_message, color="red"),
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('Cancelar', color_scheme='gray', variant='soft')
                ),
                spacing="3",
                margin_top='16px',
                justify="end"
            ),
            style={'width': '300px'}
        ),
    )


def delete_user_dialogo_component(username: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar Usuario'),
            rx.dialog.description(
                'Está seguro de querer eliminar el usuario' + username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        'Confirmar', on_click=UserState.delete_user_by_email(username)),
                ),
                spacing='3',
                margin='10px',
                justify='end'
            )
        )
    )

app = rx.App()
# app.add_page(index)
