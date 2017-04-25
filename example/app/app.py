from flask import Flask
from flask_fileupload import FlaskFileUpload

app = Flask(__name__)
app.config.from_object("config")

fue = FlaskFileUpload(app)


@fue.auth_loader
def auth_loader():
    pass
    #return redirect("https://google.de")

