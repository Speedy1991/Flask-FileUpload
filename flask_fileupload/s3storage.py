from werkzeug.utils import secure_filename
import boto3
import re
from .storage import StorageExists, StorageNotAllowed,\
    StorageNotExists

class S3Storage(object):

    def __init__(self, app):
        self.bucket_name = app.config.get("FILEUPLOAD_S3_BUCKET", "flask_fileupload")
        self.allowed = app.config.get("FILEUPLOAD_ALLOWED_EXTENSIONS", list())
        self.all_allowed = app.config.get("FILEUPLOAD_ALLOW_ALL_EXTENSIONS",
                                          False)
        self.snake_case = app.config.get("FILEUPLOAD_CONVERT_TO_SNAKE_CASE",
                                         False)
        self.s3 = boto3.client('s3')
        response = self.s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        if self.bucket_name not in buckets:
            self.s3.create_bucket(Bucket=self.bucket_name)
        self.bucket = self.s3.Bucket(self.bucket_name)

    def get_existing_files(self):
        return [f.key for f in self.bucket.obects.all()]

    def store(self, filename, file_data):
        filename = secure_filename(filename)

        if self.snake_case:
            filename = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', filename)
            filename = re.sub('([a-z0-9])([A-Z])', r'\1_\2', filename).lower()

        if self._exists(filename):
            raise StorageExists()

        if self.all_allowed or any(filename.endswith('.' + x) for x in self.allowed):
            self.s3.put_object(Bucket=self.bucket_name,
                               Key=filename,
                               Body=file_data)
        else:
            raise StorageNotAllowed()
        return filename

    def delete(self, filename):
        if not self._exists(filename):
            raise StorageNotExists()
        else:
            self.s3.delete_object(Bucket=self.bucket_name,
                                  Key=filename)

    def get_abs_img_path(self):
        return '{}/{}'.format(self.s3.meta.endpoint_url, self.bucket_name)

    def _exists(self, filename):
        objs = list(self.bucket.objects.filter(Prefix=filename))
        if len(objs) > 0 and objs[0].key == filename:
            return True
        else:
            return False

