Flask-FileUpload
----------------

A simple file upload flask extension.

- Previews
- Easy link copy
- Delete and Upload with 3 clicks
- Renaming of the file before uploading

Install
-------

```pip install flask_fileupload```

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

Previews
--------
