import unittest
from unittest.mock import patch, mock_open
import os
from commands import CommandExecutor


class TestCommandExecutor(unittest.TestCase):

    def setUp(self):
        """Настройка тестового окружения"""
        self.vfs_root = os.path.join(os.getcwd(), "test_vfs")
        if not os.path.exists(self.vfs_root):
            os.makedirs(self.vfs_root)

        os.makedirs(os.path.join(self.vfs_root, "dir1"), exist_ok=True)
        with open(os.path.join(self.vfs_root, "dir1", "file1.txt"), "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

        self.executor = CommandExecutor(self.vfs_root, "/")

    @patch("sys.stdout")
    def test_tac(self, mock_stdout):
        """Тестируем команду tac"""
        with patch("builtins.open", mock_open(read_data="Line 1\nLine 2\nLine 3")):
            output = self.executor.tac("file1.txt")
            self.assertEqual(output, "Line 3\nLine 2\nLine 1\n")

    def test_mv(self):
        """Тестируем команду mv"""
        # Создаем файл для теста
        with open(os.path.join(self.vfs_root, "file_to_move.txt"), "w") as f:
            f.write("Test file")

        result = self.executor.mv("file_to_move.txt", "dir1/file_to_move.txt")
        self.assertEqual(result, "Moved 'file_to_move.txt' to 'dir1/file_to_move.txt'.")

    def tearDown(self):
        """Очистка тестовой среды"""
        for root_dir in os.listdir(self.vfs_root):
            dir_path = os.path.join(self.vfs_root, root_dir)
            if os.path.isdir(dir_path):
                for file in os.listdir(dir_path):
                    os.remove(os.path.join(dir_path, file))
                os.rmdir(dir_path)
        os.rmdir(self.vfs_root)


if __name__ == "__main__":
    unittest.main()
