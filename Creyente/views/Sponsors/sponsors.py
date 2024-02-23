import reflex as rx
import Creyente.constants as const
from Creyente.components.title import title
from Creyente.components.link_sponsor import Link_sponsor
from Creyente.estilo.estilo import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Creyente & Hijos"),
       
          rx.hstack(
               Link_sponsor(
                    "carpinteria.jpg",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
               Link_sponsor(
                    "logo_c.png",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
           spacing=Size.BIG.value,
           #columns=[1,2],
          ),
       
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
    