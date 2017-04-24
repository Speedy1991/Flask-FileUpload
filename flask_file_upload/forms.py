from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField


class UploadForm(FlaskForm):
    ALLOWED_EXTENSIONS = ["jpeg", "jpg", "png", "gif"]

    upload_name = StringField(
        'Name', validators=[DataRequired()],
        render_kw={"placeholder": "Images: " + ", ".join(ALLOWED_EXTENSIONS)})

    upload_img = FileField(
        validators=[FileRequired(),
                    FileAllowed(ALLOWED_EXTENSIONS, 'Images/gif`s only!')])
