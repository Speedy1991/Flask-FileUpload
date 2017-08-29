from flask_fileupload.storage.utils import split_filename, lower_file_extension, convert_to_snake_case, InvalidExtension
import pytest
from unittest import TestCase


class TestPermissions(TestCase):
    def test_lower_file_extension(self):
        self.assertEqual(lower_file_extension("dummy.png"), "dummy.png")
        self.assertEqual(lower_file_extension("dummy.pNg"), "dummy.png")
        self.assertEqual(lower_file_extension("dummy.PNg"), "dummy.png")
        self.assertEqual(lower_file_extension("dummy.PNG"), "dummy.png")

    def test_split_filenames(self):
        with pytest.raises(InvalidExtension):
            split_filename("dummypng")
        with pytest.raises(InvalidExtension):
            split_filename("dummypng.")
        filename, extension = split_filename("dummy.png")
        self.assertEqual(filename, "dummy")
        self.assertEqual(extension, ".png")

        filename, extension = split_filename("dummy.png.jpg")
        self.assertEqual(filename, "dummy.png")
        self.assertEqual(extension, ".jpg")

    def test_snake_case(self):
        self.assertEqual(convert_to_snake_case("dummyABC.png"), "dummy_abc.png")
        self.assertEqual(convert_to_snake_case("dummyEFG.png"), "dummy_efg.png")
        self.assertEqual(convert_to_snake_case("dummyHiJ.png"), "dummy_hi_j.png")
