from flask_login import LoginManager
from flask import Flask
from flask_fileupload import FlaskFileUpload
from unittest import TestCase


class TestPermissions(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"] = "test"
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.config['TESTING'] = True

        login_manager = LoginManager(self.app)
        
        @login_manager.user_loader
        def load_user(user_id):
            return None
        
        self.login_manager = login_manager
        self.ffu = FlaskFileUpload(self.app)
        self.client = self.app.test_client()

    def test_permissions(self):
        # Not logged in
        response = self.client.get("/upload/")
        self.assertEqual(response.status_code, 401)
        response = self.client.get("/upload/delete/abc")
        self.assertEqual(response.status_code, 401)
