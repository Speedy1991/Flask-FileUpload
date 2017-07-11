from flask import Blueprint, render_template, flash, redirect, request, url_for
from .forms import UploadForm
from .storage import StorageNotAllowed, StorageExists, StorageNotExists
from flask_login import login_required


def create_blueprint(import_name, app, storage):

    bp = Blueprint("flask_fileupload", import_name,
                   template_folder="templates",
                   static_folder="static",
                   static_url_path="/static",
                   )

    @bp.route("/", methods=["GET", "POST"])
    @login_required
    def upload():
        form = UploadForm()
        if form.validate_on_submit():
            try:
                filename = storage.store(form.upload_name.data, form.upload_img.data)
            except (StorageNotAllowed, StorageExists) as e:
                flash(str(e), category="danger")
                return redirect(request.url)
            else:
                flash("Image saved: " + filename, category="info")

            return redirect(request.url)

        img_abs_path = storage.get_abs_path()
        return render_template("fileupload/upload.html",
                               existing_files=storage.get_existing_files(),
                               form=form,
                               img_abs_path=img_abs_path)

    @bp.route("/delete/<filename>", methods=["GET"])
    @login_required
    def upload_delete(filename):
        try:
            storage.delete(filename)
            flash("File removed: " + filename, category="info")
        except StorageNotExists as e:
            flash(str(e))

        return redirect(url_for("flask_fileupload.upload"))

    return bp

