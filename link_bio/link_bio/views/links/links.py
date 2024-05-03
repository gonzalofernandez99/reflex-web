import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.button("Linkeding", kind="link", href="https://www.linkedin.com/in/fernandez-gonzalo/"),
    )