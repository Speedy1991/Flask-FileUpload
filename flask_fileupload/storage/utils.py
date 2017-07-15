import re


def convert_to_snake_case(filename):
    filename = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', filename)
    filename = re.sub('([a-z0-9])([A-Z])', r'\1_\2', filename).lower()
    return filename
