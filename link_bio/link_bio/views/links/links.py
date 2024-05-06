import reflex as rx
import link_bio.constants as const
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Color, Spacing
from link_bio.state.PageState import PageState


def index_links() -> rx.Component:
    return rx.vstack(
        title("Yotube"),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),

        title("Linkedin"),
        link_button(
            "Linkedin - Contacto",
            "Aquí puedes ver los lugares en donde estoy trabajando",
            "/icons/git.svg",
            const.LINKEDIN_URL
        ),
        
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        )
    )