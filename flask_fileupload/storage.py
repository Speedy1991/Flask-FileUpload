from werkzeug.utils import secure_filename
import os
from .utils import convert_to_snake_case


class StorageNotAllowed(Exception):
    def __init__(self):
        super(StorageNotAllowed, self).__init__("This file extension is not allowed.")


class StorageExists(Exception):
    def __init__(self):
        super(StorageExists, self).__init__("File already exists, choose an other name")


class StorageNotExists(Exception):
    def __init__(self):
        super(StorageNotExists, self).__init__("File does not exist")


class AbstractStorage(object):
    def __init__(self, app):
        self.allowed = app.config.get("FILEUPLOAD_ALLOWED_EXTENSIONS", list())
        self.all_allowed = app.config.get("FILEUPLOAD_ALLOW_ALL_EXTENSIONS", False)
        self.img_folder = app.config.get("FILEUPLOAD_IMG_FOLDER", "upload")
        self.snake_case = app.config.get("FILEUPLOAD_CONVERT_TO_SNAKE_CASE", False)
        self.app = app

    def get_existing_files(self):
        raise NotImplementedError()

    def store(self, filename, file_data):
        raise NotImplementedError()

    def delete(self, filename):
        raise NotImplementedError()


class Storage(AbstractStorage):

    def __init__(self, app):
        super(Storage, self).__init__(app)
        self.abs_img_folder = os.path.join(app.root_path, "static", self.img_folder)
        if not os.path.exists(self.abs_img_folder):
            os.makedirs(self.abs_img_folder)

    def get_existing_files(self):
        return [f for f in os.listdir(self.abs_img_folder)]

    def _get_abs_file(self, filename):
        return os.path.join(self.abs_img_folder, filename)

    def store(self, filename, file_data):
        filename = secure_filename(filename)
        if self.snake_case:
            filename = convert_to_snake_case(filename)

        if filename in self.get_existing_files():
            raise StorageExists()

        if self.all_allowed or any(filename.endswith('.' + x) for x in self.allowed):
            file_data.save(self._get_abs_file(filename))
        else:
            raise StorageNotAllowed()

        return filename

    def delete(self, filename):
        existing_files = self.get_existing_files()
        if filename not in existing_files:
            raise StorageNotExists()
        else:
            os.remove(self._get_abs_file(filename))
