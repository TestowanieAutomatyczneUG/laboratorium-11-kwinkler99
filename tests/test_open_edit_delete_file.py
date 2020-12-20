from unittest import TestCase
from unittest.mock import patch, mock_open, MagicMock
from assertpy import assert_that

from src.sample.open_edit_delete_file import File


class TestFile(TestCase):
    @patch("builtins.open", mock_open(read_data='test mock'))
    def test_open_file(self):
        openFile = File('/fake/file/path').open()
        assert_that(openFile).is_equal_to(['test mock'])

    def test_edit_file(self):
        fake_file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('builtins.open', mock_open()) as file:
            File(fake_file_path).edit(content)

            file.assert_called_once_with(fake_file_path, 'w')

    @patch('src.sample.open_edit_delete_file.os')
    def test_delete_file(self, mock_os):
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = True

        File("fake/file/path").delete()
        mock_os.remove.assert_called_once_with("fake/file/path")

    @patch('src.sample.open_edit_delete_file.os')
    def test_raises_delete_file(self, mock_os):
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = False

        self.assertRaises(Exception, File("fake/file/path").delete())
