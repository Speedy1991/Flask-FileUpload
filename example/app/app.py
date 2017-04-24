from flask import Flask, render_template
from flask_file_upload import FlaskFileUpload

app = Flask(__name__)
app.config.from_object("config")
fue = FlaskFileUpload(app)
