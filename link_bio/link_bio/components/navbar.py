import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Gonzalo Fernandez",
            height="40px",
        ),
        position="sticky",
        z_index="999"
    )