[![Build Status](https://travis-ci.org/Speedy1991/Flask-FileUpload.svg?branch=master)](https://travis-ci.org/Speedy1991/Flask-FileUpload)

Flask-FileUpload
----------------

A simple file upload flask extension.

- Previews
- Easy link copy
- Delete and Upload with 3 clicks
- Renaming of the file before uploading
- AWS S3 support
- Google Cloud Storage support

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

__S3 Storage__
```python
FILEUPLOAD_S3_BUCKET = 'sample-bucket-name'                         # name of the S3 bucket
FILEUPLOAD_S3_ACL = 'public-read'                                   # S3 permission
```

__S3 permission options:__

- public-read
- private
- public-read-write
- authenticated-read
- aws-exec-read
- bucket-owner-read
- bucket-owner-full-control

__Google Cloud Storage__
```python
FILEUPLOAD_GCS_BUCKET = 'sample-bucket-name'                         # name of the GCS bucket
FILEUPLOAD_GCS_ACL = 'publicRead'                                    # GCS permissions
FILEUPLOAD_GCS_STORAGE_CLASS = 'REGIONAL'                            # bucket storage class
FILEUPLOAD_GCS_BUCKET_LOCATION = 'us-west2'                          # bucket location
```

__Google Cloud Storage permission options:__

- private
- bucketOwnerRead
- bucketOwnerFullControl
- projectPrivate
- authenticatedRead
- publicRead
- publicReadWrite

### [Google Cloud Storage usage documentation](doc/google_cloud_storage.md)

jinja2 method and filter 
------------------------
 
```python 
fu_get_existing_files 
fu_filename 
```` 
They can be used _everywhere_ in your jinja template for e.g: list all available files. Combined you can do something like: 
 
```python 
<ul> 
  {% for file in fu_get_existing_files() %} 
    <li><a href="{{ file }}">{{ file|fu_filename }} </a></li> 
  {% endfor %} 
</ul> 
``` 
 
HowTo
-----
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

Change Storage
--------------

```python
from flask_fileupload import FlaskFileUpload
from flask_fileupload.storage.s3storage import S3Storage
...
s3storage = S3Storage()
ffu = FlaskFileUpload(app, s3storage)
```

If no storage is provided, the default storage will be taken

Previews
--------

![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/overview.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/sort_and_searchable.png)
----
![](https://github.com/Speedy1991/Flask-FileUpload/blob/master/doc/img/zoom.png)

