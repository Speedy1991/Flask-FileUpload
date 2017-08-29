import re


class InvalidExtension(Exception):
    pass

# TODO: Docs


def split_filename(filename):
    last_dot = filename.rfind(".")
    if last_dot == -1:
        raise InvalidExtension()
    extension = filename[last_dot:]
    if len(extension) == 1:  # Just a dot
        raise InvalidExtension()
    return filename[:last_dot], extension


def convert_to_snake_case(filename):
    filename, extension = split_filename(filename)
    filename = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', filename)
    filename = re.sub('([a-z0-9])([A-Z])', r'\1_\2', filename).lower()
    return filename + extension


def lower_file_extension(filename):
    filename, extension = split_filename(filename)
    return filename + extension.lower()
