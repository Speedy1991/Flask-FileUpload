import os

from werkzeug.utils import secure_filename
from flask import url_for
from .utils import convert_to_snake_case
from . import AbstractStorage, StorageExists, StorageNotExists, StorageNotAllowed


class LocalStorage(AbstractStorage):

    def __init__(self, app):
        super(LocalStorage, self).__init__(app)
        self.img_folder = app.config.get("FILEUPLOAD_LOCALSTORAGE_IMG_FOLDER", "upload")
        self.img_folder = self.img_folder if self.img_folder.endswith("/") else self.img_folder + "/"
        self.abs_img_folder = os.path.join(app.root_path, "static", self.img_folder)
        if not os.path.exists(self.abs_img_folder):
            os.makedirs(self.abs_img_folder)

    def get_existing_files(self):
        return [f for f in os.listdir(self.abs_img_folder)]

    def get_base_path(self):
        return url_for("static", filename=self.img_folder)

    def store(self, filename, file_data):
        filename = secure_filename(filename)
        if self.snake_case:
            filename = convert_to_snake_case(filename)

        if filename in self.get_existing_files():
            raise StorageExists()

        if self.all_allowed or any(filename.endswith('.' + x) for x in self.allowed):
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
