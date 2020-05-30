import os

from flask import url_for
from . import AbstractStorage, StorageExists, StorageNotExists


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

    def _store(self, filename, file_data):
        if filename in self.get_existing_files():
            raise StorageExists()
        file_data.save(os.path.join(self.abs_img_folder, filename))
        return filename

    def _delete(self, filename):
        if filename not in self.get_existing_files():
            raise StorageNotExists()
        os.remove(os.path.join(self.abs_img_folder, filename))
