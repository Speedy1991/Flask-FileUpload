from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileField


class UploadForm(FlaskForm):

    upload_name = StringField('Name', validators=[DataRequired()])
    upload_img = FileField(validators=[FileRequired()])
