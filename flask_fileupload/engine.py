from .storage import Storage


class FlaskFileUpload(object):

    def __init__(self, app=None):
        self.app = None
        self.config = None
        self.storage = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        self.app = app
        self.storage = Storage(app)

        from .views import create_blueprint
        bp = create_blueprint(__name__, app=app, storage=self.storage)

        self.app.register_blueprint(
            bp,
            url_prefix=app.config.get("FILE_UPLOAD_PREFIX", "/upload")
        )


