import os
from pathlib import Path
import shutil


class FileOrganizer:
    def __get_only_files(path=None):
        files = [os.path.abspath(os.path.join(path, f)).lower()
                 for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        current_py_file_name = os.path.abspath(__file__).lower()
        try:
            files.remove(current_py_file_name)
        except ValueError:
            pass
        return files

    def __create_directories_and_move_files(path):
        files = FileOrganizer.__get_only_files(path)
        folders = set()
        for file in files:
            _, file_extension = os.path.splitext(file)
            folder_path = os.path.join(path, file_extension[1:])
            if file_extension[1:] in folders:
                shutil.move(file, folder_path)
            else:
                Path(folder_path).mkdir(parents=True, exist_ok=True)
                shutil.move(file, folder_path)
                folders.add(file_extension[1:])

    @staticmethod
    def organize_files(path: str = None):
        """
        Сreates directories for all extensions at the specified path and moves files there.
        If you do not pass an argument (path), it will work in the current directory.
        """
        FileOrganizer.__create_directories_and_move_files(path)


def main():
    path = input('Enter path: ').strip()
    if path == '' or not path:
        path = Path(__file__).parent.resolve()
    FileOrganizer.organize_files(path)
    print('Complete')


if __name__ == "__main__":
    main()
