from blinkpy import blinkpy
from datetime import datetime, timedelta

from watcher.constants import INCEPTION_TIME
from watcher.helpers.filesystem import create_directories_if_non_existent


class Downloader:
    def __init__(self, username, password, downloads_folder):
        self.downloads_folder = downloads_folder

        self.blink = blinkpy.Blink(username=username, password=password)
        self.blink.start()

    def download_today(self):
        midnight = datetime.utcnow().replace(
            hour=0, minute=0, second=0, microsecond=0
        ) - timedelta(days=1)

        create_directories_if_non_existent(self.downloads_folder)
        self.blink.download_videos(path=self.downloads_folder, since=str(midnight))

    def download_all(self):
        self.blink.download_videos(path=self.downloads_folder, since=INCEPTION_TIME)
