class StorageNotAllowed(Exception):
    def __init__(self):
        super(StorageNotAllowed, self).__init__("This file extension is not allowed.")


class StorageExists(Exception):
    def __init__(self):
        super(StorageExists, self).__init__("File already exists, choose an other name")


class StorageNotExists(Exception):
    def __init__(self):
        super(StorageNotExists, self).__init__("File does not exist")


class AbstractStorage(object):
    def __init__(self, app):
        self.allowed = app.config.get("FILEUPLOAD_ALLOWED_EXTENSIONS", list())
        self.all_allowed = app.config.get("FILEUPLOAD_ALLOW_ALL_EXTENSIONS", False)
        self.snake_case = app.config.get("FILEUPLOAD_CONVERT_TO_SNAKE_CASE", False)
        self.app = app

    def get_existing_files(self):
        """
        :return:  list of files
        """
        raise NotImplementedError()

    def get_abs_path(self):
        """
        :return: base path where the image can be found
        """
        raise NotImplementedError()

    def store(self, filename, file_data):
        raise NotImplementedError()

    def delete(self, filename):
        raise NotImplementedError()
