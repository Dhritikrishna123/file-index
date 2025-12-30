#!/usr/bin/env python3
from cli.welcome import show_welcome
from cli.style import Style
from core.scan import Scan
from core.search import Search
import sys


style = Style()


def scan_cmd(args):
    if not args:
        style.preety(
            " Usage: fileindex scan <path> ",
            width=70,
            char=" ",
            style=Style.WARNING,
        )
        return

    path = args[0]

    try:
        scanner = Scan(path)
        records = scanner.run()

        style.preety(
            f" Indexed {len(records)} files ",
            width=70,
            char=" ",
            style=Style.SUCCESS,
        )

    except (FileNotFoundError, NotADirectoryError) as e:
        style.preety(
            f" {e} ",
            width=70,
            char="!",
            style=Style.ERROR,
        )


def search_cmd(args):
    if len(args) < 2:
        style.preety(
            " Usage: fileindex search <path> <query> ",
            width=70,
            char=" ",
            style=Style.WARNING,
        )
        return

    path = args[0]
    query = args[1]

    try:
        records = Scan(path).run()
        search = Search(records)
        results = search.by_name(query)

        style.preety(
            f" Found {len(results)} results ",
            width=70,
            char=" ",
            style=Style.INFO,
        )

        for r in results[:10]:  # limit output
            print(r["path"])

    except (FileNotFoundError, NotADirectoryError) as e:
        style.preety(f" {e} ", 70, "!", Style.ERROR)


def dispatch():
    args = sys.argv[1:]

    if not args:
        show_welcome()
        return

    command = args[0]
    command_args = args[1:]

    if command == "scan":
        scan_cmd(command_args)
    elif command == "search":
        search_cmd(command_args)
    else:
        style.preety(
            f" Unknown command: {command} ",
            width=70,
            char="!",
            style=Style.ERROR,
        )


def main():
    dispatch()


if __name__ == "__main__":
    main()
