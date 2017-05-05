from flask_login import LoginManager
from flask import Flask
from flask_fileupload import FlaskFileUpload
from unittest import TestCase
import shutil
import io
from werkzeug.datastructures import FileStorage
import pytest
from flask_fileupload.storage import StorageExists, StorageNotAllowed, StorageNotExists


class TestPermissions(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"] = "test"
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.config['TESTING'] = True
        self.app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg"]

        self.login_manager = LoginManager(self.app)
        self.ffu = FlaskFileUpload(self.app)

        self.dummy_stream = io.BytesIO(b"some initial text data")
        self.fs = FileStorage(self.dummy_stream, "dummy.png")

    def tearDown(self):
        shutil.rmtree(self.ffu.storage.abs_img_folder, ignore_errors=True)

    def test_store_file(self):
        self.ffu.storage.store("dummy.jpg", self.fs)
        self.ffu.storage.store("dummy.png", self.fs)

    def test_delete_file(self):

        self.ffu.storage.store("dummy.png", self.fs)
        self.ffu.storage.delete("dummy.png")

    def test_exception_file_exists(self):
        self.ffu.storage.store("dummy.png", self.fs)
        with pytest.raises(StorageExists):
            self.ffu.storage.store("dummy.png", self.fs)

    def test_exception_file_not_allowed(self):
        with pytest.raises(StorageNotAllowed):
            self.ffu.storage.store("dummy.txt", self.fs)

    def test_exception_file_not_exists(self):
        with pytest.raises(StorageNotExists):
            self.ffu.storage.delete("abc.de")
