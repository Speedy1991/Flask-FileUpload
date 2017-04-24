
class FlaskFileUpload(object):

    def __init__(self, app=None):
        self.app = None
        self.config = None
        self.auth_callback = None

        if app is not None:
            self.init_app(app)

    def auth_loader(self, callback):
        self.auth_callback = callback
        return callback

    def init_app(self, app):
        self.app = app
        self.config = self.app.config

        from .views import create_blueprint
        bp = create_blueprint(__name__, url_prefix=self.app.config.get("FLASK_FILEUPLOAD_PREFIX", "/upload"))

        @bp.before_request
        def before_request():
            if self.auth_callback is not None:
                return self.auth_callback()

        self.app.register_blueprint(
            bp,
            url_prefix=self.config.get("FILE_UPLOAD_PREFIX")
        )


