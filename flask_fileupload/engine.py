from .storage.storage import LocalStorage


class FlaskFileUpload(object):

    def __init__(self, app=None, storage=None):
        self.app = None
        self.storage = storage
        self.prefix = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        self.app = app
        self.storage = self.storage or LocalStorage(app)
        self.prefix = app.config.get("FILEUPLOAD_PREFIX", "/upload")

        from .views import create_blueprint
        bp = create_blueprint(__name__, app=app, storage=self.storage)

        self.app.register_blueprint(
            bp,
            url_prefix=self.prefix
        )
