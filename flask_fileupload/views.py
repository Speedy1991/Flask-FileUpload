from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask import current_app as app
import os
from .forms import UploadForm
from werkzeug.utils import secure_filename
from flask_login import login_required


def _get_abs_img_path():
    ROOT = os.path.sep.join(app.root_path.split(os.path.sep))
    ABS_IMG_FOLDER = os.path.join(
        ROOT, app.config.get("IMG_FOLDER", os.path.join("static", "upload")))

    if not os.path.exists(ABS_IMG_FOLDER):
        os.makedirs(ABS_IMG_FOLDER)

    return ABS_IMG_FOLDER


#@login_required
def upload():
    existing_files = list(sorted([f for f in os.listdir(_get_abs_img_path())]))
    filename = ""
    form = UploadForm()
    if form.validate_on_submit():
        uploaded_img = form.upload_img.data
        filename = secure_filename(form.upload_name.data)

        if not any(filename.endswith('.' + x) for x
                   in UploadForm.ALLOWED_EXTENSIONS):
            flash("This file extension is not allowed."
                  "Use one of these: {ext}"
                  .format(ext=" ,".join(UploadForm.ALLOWED_EXTENSIONS)),
                  category="danger")
            return redirect(request.url)

        if filename in existing_files:
            flash("File already exists, choose an other name",
                  category="warning")
            return redirect(request.url)

        uploaded_img.save(os.path.join(_get_abs_img_path(), filename))
        flash("Image saved: " + filename, category="info")

        return redirect(request.url)

    if form.errors:
        flash("Errors on Form. Check if you provide all needed data!",
              category="danger")

    return render_template("flask_file_upload/upload.html",
                           existing_files=existing_files,
                           new_file=filename,
                           form=form)


#@login_required
def upload_delete(filename):
    existing_files = list(sorted([f for f in os.listdir(_get_abs_img_path())]))
    if filename not in existing_files:
        flash("File does not exist", category="danger")
    else:
        os.remove(os.path.join(_get_abs_img_path(), filename))
        flash("File removed: " + filename, category="info")
    return redirect(url_for("flask_file_upload.upload"))


def create_blueprint(import_name):
    fileupload_app = Blueprint("flask_file_upload", import_name,
                               template_folder="templates",
                               static_folder="static",
                               static_url_path="/static",
                               url_prefix="/upload"
                               )

    fileupload_app.add_url_rule("/",
                                view_func=upload,
                                methods=["GET", "POST"])

    fileupload_app.add_url_rule("/delete/<filename>",
                                view_func=upload_delete,
                                methods=["GET"]
                                )

    return fileupload_app

