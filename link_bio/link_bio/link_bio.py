import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width="600px",
            width="100%"      
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="GonzaloFernandez | Web personal de Gonzalo Fernández",
             description="Hola, mi nombre es Gonzalo Fernandez. Soy ingeniero de software, desarrollador freelance full-stack.",
             image="avatar.jpg")
app.compile()