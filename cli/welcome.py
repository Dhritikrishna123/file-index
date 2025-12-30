from cli.style import Style


BANNER = [
    "███████╗██╗██╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██╗  ██╗",
    "██╔════╝██║██║     ██╔════╝██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝",
    "█████╗  ██║██║     █████╗  ██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ ",
    "██╔══╝  ██║██║     ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ ",
    "██║     ██║███████╗███████╗██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗",
    "╚═╝     ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝",
]


def show_welcome():
    style = Style()

    print()

    banner_style = Style.apply(Style.BOLD, Style.BRIGHT_GREEN)
    subtitle_style = Style.apply(Style.DIM, Style.BRIGHT_YELLOW)
    option_style = Style.apply(Style.BRIGHT_CYAN)
    hint_style = Style.apply(Style.DIM)

    # Banner
    for line in BANNER:
        style.preety(line, width=90, char=" ", style=banner_style)

    print()

    # Subtitle
    style.preety(
        " Fast Local Indexing And Search ",
        width=90,
        char="-",
        style=subtitle_style,
    )

    print()

    # Options (informational, not interactive)
    style.preety(" scan   → index a directory", width=90, char=" ", style=option_style)
    style.preety(" search → find files from index", width=90, char=" ", style=option_style)

    print()

    # Usage hint
    style.preety(
        " Usage: fileindex scan <path> | fileindex search <query> ",
        width=90,
        char=" ",
        style=hint_style,
    )

    print()
