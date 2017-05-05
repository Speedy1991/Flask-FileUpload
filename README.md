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
FILEUPLOAD_IMG_FOLDER="folder"                                      # Where to store the images
FILEUPLOAD_PREFIX="/any/prefix/u/want"                              # Blueprint prefix
FILEUPLOAD_ALLOWED_EXTENSIONS=["list", "of", "file", "extensions"]  # Allow only these extensions
FILEUPLOAD_ALLOW_ALL_EXTENSIONS=True                                # Allow all extensions
```

Standalone
----------
```python
from flask import Flask
from flask_fileupload import FlaskFileUpload

app = Flask(__name__)
app.config.from_object("config")
ffu = FlaskFileUpload(app)
```

Interacting with Flask-Blogging
-------------------------------


This plugin was writen and created out of my pullrequest on [https://github.com/gouthambs/Flask-Blogging/pull/95](https://github.com/gouthambs/Flask-Blogging/pull/95)

It integrates great with [https://github.com/gouthambs/Flask-Blogging](https://github.com/gouthambs/Flask-Blogging/pull/95)

1. Create a fileupload folder in your _templates_ and copy the _base.html_ from Flask-Blogging. The Blocknaming is (atm) the same.
2. Register your app with e.g:
```python
from flask import Flask
from flask_blogging import SQLAStorage, BloggingEngine
from flask_fileupload import FlaskFileUpload

app = Flask(__name__)
app.config.from_object("config")
ffu = FlaskFileUpload(app)

from blog.models import db
sql_storage = SQLAStorage(db=db)

blog_engine = BloggingEngine(app, sql_storage)
```
3. You can ref the extension anywhere with:
```python
url_for("flask_fileupload.upload")
```

4. Find the extension under _/upload_

Security
--------

```python
from flask_login import LoginManager, UserMixin

lm = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@lm.user_loader
def load_user(user_id):
    return User(user_id)
```

TODO's
------
- Tests / CI /Travis
- More storages

Previews
--------

![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/overview.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/sort_and_searchable.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/zoom.png)

