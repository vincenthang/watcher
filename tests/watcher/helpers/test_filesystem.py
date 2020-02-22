from mock import patch

from tests.base import BaseTest

from watcher.constants import DEFAULT_DOWNLOADS_FOLDER
from watcher.helpers.filesystem import create_directories_if_non_existent


class TestFilesystem(BaseTest):
    def test_create_directories_if_non_existent(self):
        with patch("os.path.exists", side_effect=lambda f: False), patch(
            "os.makedirs"
        ) as mock_makedir:
            create_directories_if_non_existent(DEFAULT_DOWNLOADS_FOLDER)
            assert mock_makedir.call_count == 1

    def test_do_not_create_directories_if_exists(self):
        with patch("os.path.exists", side_effect=lambda f: True), patch(
            "os.makedirs"
        ) as mock_makedir:
            create_directories_if_non_existent(DEFAULT_DOWNLOADS_FOLDER)
            assert mock_makedir.call_count == 0
