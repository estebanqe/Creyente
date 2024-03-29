import reflex as rx
import Creyente.estilo.estilo as style
from Creyente.estilo.estilo import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        #size=Size.BIG.value,
        style=style.title_style
    )