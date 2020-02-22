from datetime import datetime, timedelta
from freezegun import freeze_time
from mock import call, patch

from watcher.constants import DEFAULT_DOWNLOADS_FOLDER, INCEPTION_TIME
from watcher.downloader import Downloader

from tests.base import BaseTest
from tests.constants import FAKE_PASSWORD, FAKE_USERNAME


class TestDownloader(BaseTest):
    def setUp(self):
        super(BaseTest, self).setUp()

        self.blink_start_patcher = patch("blinkpy.blinkpy.Blink.start")
        self.mock_blink_start = self.blink_start_patcher.start()

        self.blink_download_videos_patcher = patch(
            "blinkpy.blinkpy.Blink.download_videos"
        )
        self.mock_blink_download_videos_patcher = (
            self.blink_download_videos_patcher.start()
        )

        self.downloader = Downloader(
            username=FAKE_USERNAME,
            password=FAKE_PASSWORD,
            downloads_folder=DEFAULT_DOWNLOADS_FOLDER,
        )

    def test_download_today(self):
        now = datetime.utcnow()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) - (
            timedelta(days=1)
        )

        with freeze_time(now):
            self.downloader.download_today()

        print(datetime.utcnow())
        assert self.mock_blink_download_videos_patcher.call_args == call(
            path=DEFAULT_DOWNLOADS_FOLDER, since=str(midnight),
        )

    def test_download_all(self):
        self.downloader.download_all()

        assert self.mock_blink_download_videos_patcher.call_args == call(
            path=DEFAULT_DOWNLOADS_FOLDER, since=INCEPTION_TIME,
        )
