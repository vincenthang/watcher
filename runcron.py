import argparse

from watcher.config import get_config
from watcher.constants import DEFAULT_DOWNLOADS_FOLDER
from watcher.downloader import Downloader


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-a", "--all", action="store_true", help="download all surveillance videos"
    )
    parser.add_argument(
        "-f",
        "--folder",
        action="store",
        help="specify a downloads folder",
        default=DEFAULT_DOWNLOADS_FOLDER,
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    downloader = Downloader(
        username=get_config()["BLINK_USERNAME"],
        password=get_config()["BLINK_PASSWORD"],
        downloads_folder=args.folder,
    )

    if args.all:
        downloader.download_all()
    else:
        downloader.download_today()


if __name__ == "__main__":
    main()
