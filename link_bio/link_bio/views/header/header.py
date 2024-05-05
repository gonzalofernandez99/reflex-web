import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Gonzalo Fernandez",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/avatar.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Gonzalo Fernandez",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "@GonzaloFernandez",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "30+", "proyectos completados"
                    ),
                    rx.spacer(),
                    width="100%"
                ),
                rx.text(
                    """
                    Soy ingeniero de software y actualmente trabajo full-stack developer y automation developer.
                    Soy un apasionado por las nuevas tecnologías y por el aprendizaje continuo.
                    Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2019