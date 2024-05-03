import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        padding="20px",
        gap="20px",
    
    )


app = rx.App()
app.add_page(index)
app.compile()