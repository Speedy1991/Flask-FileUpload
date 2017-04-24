
class FlaskFileUpload(object):

    def __init__(self, app=None):
        self.app = None
        self.config = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.config = self.app.config

        from .views import create_blueprint
        file_upload_app = create_blueprint(__name__, url_prefix=self.app.config.get("FLASK_FILEUPLOAD_PREFIX", "/upload"))
        self.app.register_blueprint(
            file_upload_app,
            url_prefix=self.config.get("FILE_UPLOAD_PREFIX")
        )
