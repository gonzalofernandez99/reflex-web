import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de GonzaloFDev"
        ),
        rx.link(
            rx.box(
                f"© 2019-{datetime.date.today().year} ",
                rx.text(
                    "GonzaloFDev by Gonzalo Fernandez.",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v4.",
                padding_top=Size.DEFAULT.value
            )
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "ARGETNINA - BUENOS AIRES",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )