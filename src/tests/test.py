import unittest
from src.util.const import WAIT
from src.model.bin_day import BinDay
from src.model.bin_collections import BinCollections
from src.service.scraper import Scraper


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(WAIT, 7)

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
