import os
from google.cloud import storage
from werkzeug.utils import secure_filename
from .utils import convert_to_snake_case
from . import AbstractStorage, StorageExists, StorageNotExists, StorageNotAllowed


class GoogleCloudStorage(AbstractStorage):
    def __init__(self, app):
        super(GoogleCloudStorage, self).__init__(app)
        self.bucket_name = app.config.get("FILEUPLOAD_GCS_BUCKET", "flask_fileupload")
        self.acl = app.config.get("FILEUPLOAD_GCS_ACL", "publicRead")
        self.storage_class = app.config.get("FILEUPLOAD_GCS_STORAGE_CLASS", "REGIONAL")
        self.bucket_location = app.config.get("FILEUPLOAD_GCS_BUCKET_LOCATION", "us-west2")
        self.storage_client = storage.Client()
        if not self.storage_client.lookup_bucket(self.bucket_name):
            self.bucket = storage.Bucket(self.storage_client, self.bucket_name)
            self.bucket.create(client=self.storage_client,
                               location=self.bucket_location)
            self.bucket.storage_class = self.storage_class
            self.bucket.update()
        else:
            self.bucket = self.storage_client.get_bucket(self.bucket_name)

    def get_abs_existing_files(self):
        blobs = self.bucket.list_blobs()
        files_abs_path = [f.public_url for f in blobs]
        return files_abs_path

    def get_existing_files(self):
        return [f.name for f in self.bucket.list_blobs()]

    def store(self, filename, file_data):
        filename = secure_filename(filename)
        if self.snake_case:
            filename = convert_to_snake_case(filename)
        if self._exists(filename):
            raise StorageExists()
        if self.all_allowed or any(filename.endswith('.' + x) for x in self.allowed):
            blob = self.bucket.blob(filename)
            blob.upload_from_file(file_obj=file_data, predefined_acl=self.acl)
        else:
            raise StorageNotAllowed()
        return filename

    def get_base_path(self):
        return self.bucket.self_link + '/o/'

    def delete(self, filename):
        if not self._exists(filename):
            raise StorageNotExists()
        else:
            blob = self.bucket.blob(filename)
            blob.delete()

    def _exists(self, filename):
        return storage.Blob(bucket=self.bucket, name=filename).exists(self.storage_client)
