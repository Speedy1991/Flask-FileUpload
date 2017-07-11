[![Build Status](https://travis-ci.org/Speedy1991/Flask-FileUpload.svg?branch=master)](https://travis-ci.org/Speedy1991/Flask-FileUpload)

Flask-FileUpload
----------------

A simple file upload flask extension.

- Previews
- Easy link copy
- Delete and Upload with 3 clicks
- Renaming of the file before uploading

Install
-------

```pip install Flask-FileUpload```

Configuration
-------------
__Required__
```python
SECRET_KEY="Any Secret key u want"
```

__Optional__

```python
FILEUPLOAD_LOCALSTORAGE_IMG_FOLDER="folder"                         # Where to store the images if used the default LocalStorage
FILEUPLOAD_PREFIX="/any/prefix/u/want"                              # Blueprint prefix
FILEUPLOAD_ALLOWED_EXTENSIONS=["list", "of", "file", "extensions"]  # Allow only these extensions
FILEUPLOAD_ALLOW_ALL_EXTENSIONS=True                                # Allow all extensions
FILEUPLOAD_RANDOM_FILE_APPENDIX = True                              # Append a random 6 hash string to selected file
FILEUPLOAD_CONVERT_TO_SNAKE_CASE = True                             # Converts filenames to snake_case
```

HowTo
----------
```python
from flask import Flask
from flask_fileupload import FlaskFileUpload

app = Flask(__name__)
app.config.from_object("config")
ffu = FlaskFileUpload(app)
lm = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@lm.user_loader
def load_user(user_id):
    return User(user_id)
```


Previews
--------

![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/overview.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/sort_and_searchable.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/zoom.png)

