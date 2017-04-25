from werkzeug.utils import secure_filename
import os


class StorageNotAllowed(Exception):
    def __init__(self):
        super(StorageNotAllowed, self).__init__("This file extension is not allowed.")


class StorageExists(Exception):
    def __init__(self):
        super(StorageExists, self).__init__("File already exists, choose an other name")


class StorageNotExists(Exception):
    def __init__(self):
        super(StorageNotExists, self).__init__("File does not exist")


class Storage(object):

    def __init__(self, app):
        self.ALLOWED = app.config.get("FILEUPLOAD_ALLOWED_EXTENSIONS", list())
        self.ALLOW_ALL = app.config.get("FILEUPLOAD_ALLOW_ALL_EXTENSIONS", False)
        self.IMG_FOLDER = app.config.get("FLASK_FILEUPLOAD_IMG_FOLDER", "upload")

        self.root = app.root_path
        self.abs_img_folder = os.path.join(self.root, "static", self.IMG_FOLDER)

        self.app = app

        if not os.path.exists(self.abs_img_folder):
            os.makedirs(self.abs_img_folder)

    def get_existing_files(self):
        return [f for f in os.listdir(self.abs_img_folder)]

    def store(self, filename, file_data):
        filename = secure_filename(filename)

        if filename in self.get_existing_files():
            raise StorageExists()

        if self.ALLOW_ALL or any(filename.endswith('.' + x) for x in self.ALLOWED):
            file_data.save(os.path.join(self.abs_img_folder, filename))
        else:
            raise StorageNotAllowed()

        return filename

    def delete(self, filename):
        existing_files = self.get_existing_files()
        if filename not in existing_files:
            raise StorageNotExists()
        else:
            os.remove(os.path.join(self.abs_img_folder, filename))

    def get_abs_img_path(self):
        return self.abs_img_folder
