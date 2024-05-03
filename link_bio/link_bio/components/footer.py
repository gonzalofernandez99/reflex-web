import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(
            "Gonzalo Fernandez",
            height="40px",
        ),
    )