import reflex as rx
# from asyncio import asyncio as asyncio

def notify_component(message: str,icon_notify:str,color:str) -> rx.Component:
    return rx.callout(
        message,
        icon=icon_notify,
        style=style_notify,
        color_scheme=color
    )

style_notify = {
    'position': 'flxed',
    'top':'0px',
    'right':'0px',
    'margin':'10px 10px',
    'background-color' : 'red',
    
}