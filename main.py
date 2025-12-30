#!/usr/bin/env python3
import sys
import time

from cli.welcome import show_welcome
from cli.style import Style
from core.scan import Scan
from core.search import Search
from core.cache import IndexCache


style = Style()
cache = IndexCache()


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
        records = Scan(path).run()
        cache.save(path, records)

        style.preety(
            f" Indexed {len(records)} files ",
            width=70,
            char=" ",
            style=Style.SUCCESS,
        )

    except (FileNotFoundError, NotADirectoryError) as e:
        style.preety(f" {e} ", 70, "!", Style.ERROR)


def search_cmd(args):
    if not args:
        style.preety(
            " Usage: fileindex search <query>  OR  fileindex search <path> <query> ",
            width=70,
            char=" ",
            style=Style.WARNING,
        )
        return

    if len(args) == 1:
        query = args[0]
        path = cache.get_last_root()

        if not path:
            style.preety(
                " No cached index found. Run: fileindex scan <path> ",
                width=70,
                char="!",
                style=Style.ERROR,
            )
            return
    else:
        path = args[0]
        query = args[1]

    try:
        if cache.is_valid(path):
            data = cache.load()
            records = data["records"]
        else:
            records = Scan(path).run()
            cache.save(path, records)

        results = Search(records).by_name(query)

        style.preety(
            f" Found {len(results)} results ",
            width=70,
            char=" ",
            style=Style.INFO,
        )

        for r in results[:10]:
            print(r["path"])

    except (FileNotFoundError, NotADirectoryError) as e:
        style.preety(f" {e} ", 70, "!", Style.ERROR)


def status_cmd():
    data = cache.load()

    if not data:
        style.preety(
            " No cache found ",
            width=70,
            char="!",
            style=Style.ERROR,
        )
        return

    scanned_time = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(data["scanned_at"]),
    )

    style.preety(" Cache Status ", 70, "-", Style.INFO)
    print(f"Root        : {data['root']}")
    print(f"Files       : {data['file_count']}")
    print(f"Scanned At  : {scanned_time}")


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
    elif command == "status":
        status_cmd()
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
