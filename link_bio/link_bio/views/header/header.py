import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Gonzalo Fernandez", size="xl"),
        rx.text("@GonzaloFernandez1999"),
        rx.text("Hola mi nombre es gonzalo fernandez y soy un desarrollador de software"),
        rx.text("Soy ingeniero en sistemas computacionales y me especializo en el desarrollo de software"),
        
    )