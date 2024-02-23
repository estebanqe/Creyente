import reflex as rx
import Creyente.estilo.estilo as style
from Creyente.estilo.estilo import Size, EmSize

def Link_sponsor(imagen: str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )
    