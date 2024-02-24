import reflex as rx
import Creyente.constants as const
from Creyente.components.title import title
from Creyente.components.link_sponsor import Link_sponsor
from Creyente.estilo.estilo import Size as Size
from Creyente.estilo.color import text_color


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Ubicación"),
       
          rx.hstack(
               Link_sponsor(
                    "location.svg",
                    const.UBICACIN, 
                    "simbolo de ubicación"        
               ),
               rx.text(
                   "Av. beltran frente al campamento Panavial  San Antonio",
                   color=text_color.BLANCO.value,
                   
               ),
           spacing=Size.BIG.value,
           #columns=[1,2],
          ),
       
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
    