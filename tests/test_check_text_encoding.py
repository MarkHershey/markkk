import unittest
import sys
from pathlib import Path

# module = Path(__file__).parent.parent
# print(module)
#
# sys.path.insert(0, module)

from markkk.pyutils.check_text_encoding import *


class TestInvalidType(unittest.TestCase):
    def test_is_ascii(self):
        with self.assertRaises(Exception):
            is_ascii(100)

    def test_check_non_ascii_index(self):
        with self.assertRaises(TypeError):
            check_non_ascii_index(100)


class TestSuccess(unittest.TestCase):
    def test_ensure_no_zh_punctuation(self):
        self.assertEqual(ensure_no_zh_punctuation(u"，。/；‘’【】"), ",./;''[]")


if __name__ == "__main__":
    unittest.main()
