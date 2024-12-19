import os
import shutil

class CommandExecutor:
    def __init__(self, vfs_root, current_dir):
        """Инициализация исполнителя команд."""
        self.vfs_root = vfs_root  # Корень виртуальной файловой системы
        self.current_dir = current_dir  # Текущая директория

    def execute(self, command):
        """Выполнение команды."""
        if command.startswith("ls"):
            return self.ls()
        elif command.startswith("cd"):
            new_dir = command.split(" ", 1)[1] if " " in command else ""
            self.cd(new_dir)
            return None  # Изменение директории не требует вывода
        elif command.startswith("cat"):
            file_name = command.split(" ", 1)[1] if " " in command else ""
            return self.cat(file_name)
        elif command.startswith("tac"):
            file_name = command.split(" ", 1)[1] if " " in command else ""
            return self.tac(file_name)
        elif command.startswith("mv"):
            args = command.split(" ", 2)[1:] if len(command.split(" ")) > 1 else []
            return self.mv(*args)
        elif command == "clear":
            self.clear()
        else:
            return f"Unknown command: {command}"

    def ls(self):
        """Вывод содержимого текущей директории."""
        try:
            current_dir = os.path.normpath(self.current_dir.strip('/')) or "/"
            contents = []

            path = os.path.join(self.vfs_root, current_dir)

            if not os.path.exists(path) or not os.path.isdir(path):
                print(f"Error: Directory '{current_dir}' does not exist.")
                return

            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    contents.append(f"[Dir] {item}")
                elif os.path.isfile(item_path):
                    contents.append(item)

            if contents:
                print("\n".join(contents))
            else:
                print(f"No files or directories in '{current_dir}'.")
        except Exception as e:
            print(f"Error accessing directory contents: {e}")

    def cd(self, new_dir):
        """Изменение текущей директории."""
        if not new_dir:
            print("Error: No directory specified.")
            return

        if "//" in new_dir:
            print("Error: Invalid directory path. Double slashes are not allowed.")
            return

        if new_dir == "/" or new_dir == "\\":
            print("Error: Invalid directory path.")
            return

        if new_dir == "..":
            if self.current_dir == "/":
                print("You are already at the root directory.")
                return
            else:
                self.current_dir = os.path.dirname(self.current_dir)
                if self.current_dir == "":
                    self.current_dir = "/"
                print(f"Current directory: {self.current_dir}")
            return

        if new_dir == ".":
            print("Error: Cannot change to the current directory.")
            return

        if new_dir.startswith("/"):
            target_dir = os.path.join(self.vfs_root, new_dir.lstrip("/"))
        else:
            target_dir = os.path.join(self.vfs_root, self.current_dir.strip("/"), new_dir)

        target_dir = os.path.normpath(target_dir)

        if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
            print(f"Error: Directory '{new_dir}' does not exist.")
        else:
            self.current_dir = os.path.relpath(target_dir, self.vfs_root)
            if not self.current_dir.startswith("/"):
                self.current_dir = "/" + self.current_dir
            print(f"Current directory: {self.current_dir}")

    def cat(self, file_name):
        """Вывод содержимого файла."""
        if not file_name:
            return "Error: No file name provided."

        file_path = os.path.join(self.vfs_root, self.current_dir.strip("/"), file_name)

        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            return f"Error: File '{file_name}' does not exist."

        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file '{file_name}': {e}"

    def tac(self, file_name):
        """Вывод содержимого файла в обратном порядке строк."""
        if not file_name:
            return "Error: No file name provided."

        file_path = os.path.join(self.vfs_root, self.current_dir.strip("/"), file_name)

        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            return f"Error: File '{file_name}' does not exist."

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                return "".join(reversed(lines))
        except Exception as e:
            return f"Error reading file '{file_name}': {e}"

    def mv(self, source, destination):
        """Перемещение файлов или директорий."""
        if not source or not destination:
            return "Error: Invalid arguments for 'mv'."

        source_path = os.path.join(self.vfs_root, self.current_dir.strip("/"), source)
        dest_path = os.path.join(self.vfs_root, self.current_dir.strip("/"), destination)

        if not os.path.exists(source_path):
            return f"Error: Source '{source}' does not exist."

        try:
            # Перемещаем файл или директорию
            shutil.move(source_path, dest_path)
            return f"Moved '{source}' to '{destination}'."
        except Exception as e:
            return f"Error moving '{source}' to '{destination}': {e}"

    def clear(self):
        """Очистка экрана."""
        os.system("cls" if os.name == "nt" else "clear")
