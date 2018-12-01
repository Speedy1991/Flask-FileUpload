# Google Cloud Storage

> To start using google cloud storage in your project you must install **google-cloud-storage** library:  
```pip install google-cloud-storage```

Related files: [**flask_fileupload/storage/gcstorage.py**](/../../blob/master/flask_fileupload/storage/gcstorage.py)

**Configuration parameters:**
1. Permission options aka Predefined ACLs([more info](https://cloud.google.com/storage/docs/access-control/lists)):  
   **Config parameter name** - `FILEUPLOAD_GCS_ACL`  
   **Default value** - `publicRead`
   - private
   - bucketOwnerRead
   - bucketOwnerFullControl         
   - projectPrivate                         
   - authenticatedRead
   - publicRead
   - publicReadWrite

2. Storage classes([more info](https://cloud.google.com/storage/docs/storage-classes)):  
   **Config parameter name** - `FILEUPLOAD_GCS_STORAGE_CLASS`  
   **Default value** - `REGIONAL`
   - MULTI_REGIONAL
   - REGIONAL
   - NEARLINE
   - COLDLINE
   - STANDARD `- equivalent to either Multi-Regional Storage or Regional Storage`  
   **Warning** - `Some storage classes can only be used in a certain type of location.`
      * `You must store Regional Storage object data in a regional location, such as us-east1.`
      * `You must store Multi-Regional Storage object data in a multi-regional location (which includes dual-regional locations) such as eu.`
      * `You can store Nearline Storage and Coldline Storage object data in any location.`

3. Bucket locations([more info](https://cloud.google.com/storage/docs/locations)):  
   **Config parameter name** - `FILEUPLOAD_GCS_BUCKET_LOCATION`  
   **Default value** - `us-west2`

4. Bucket name([more info](https://cloud.google.com/storage/docs/naming)):  
   **Config parameter name** - `FILEUPLOAD_GCS_BUCKET`  
   **Default value** - `flask_fileupload`

## Preparation stage
* Choose a project you'll work with
* [Go to the console](https://console.cloud.google.com/apis/library/storage-api.googleapis.com) and enable **Google Cloud Storage JSON API** if it doesn't yet.
* [Create](https://cloud.google.com/iam/docs/service-accounts) a service account for your project and download *.json file with credentials.
* Set **Storage Admin** role for you service account, or more granular permissions.

## Usage
* Install all requirements for your project and **google-cloud-storage** library as well.
* Set environment variable `GOOGLE_APPLICATION_CREDENTIALS` with path to your service account creadentials file in a terminal or in your code:
```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/user/app/credentials.json"
```  
* import class **GoogleCloudStorage** :
```python
from flask_fileupload.storage.gcstorage import GoogleCloudStorage
```
* And now you can use it! For example:
```python
from flask_fileupload import FlaskFileUpload
from flask_fileupload.storage.gcstorage import GoogleCloudStorage
...
gcstorage = GoogleCloudStorage(app)
ffu = FlaskFileUpload(app, storage=gcstorage)
```
