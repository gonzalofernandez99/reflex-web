import reflex as rx
from link_bio.components.link_button import link_button
def links() -> rx.Component:
    return rx.vstack(
        link_button(),
        link_button(),
        link_button(),
        link_button()
    )