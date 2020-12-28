import sys
import unittest
from pathlib import Path

from markkk.pyutils import *


class TestInvalidType(unittest.TestCase):
    def test_is_ascii(self):
        with self.assertRaises(Exception):
            is_ascii(100)

    def test_check_non_ascii_index(self):
        with self.assertRaises(TypeError):
            check_non_ascii_index(100)


class TestSuccess(unittest.TestCase):
    def test_ensure_no_zh_punctuation(self):
        before = u"，。：；"
        after = ",.:;"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"《》/？！"
        after = "<>/?!"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"‘’"
        after = "''"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"“”"
        after = '""'
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"【】「」"
        after = "[]{}"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"、｜"
        after = ",|"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"=+"
        after = "=+"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"——"
        after = "--"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"（）"
        after = "()"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"……"
        after = "......"
        self.assertEqual(ensure_no_zh_punctuation(before), after)
        before = u"～·"
        after = "~-"
        self.assertEqual(ensure_no_zh_punctuation(before), after)

    def test_is_ascii(self):
        self.assertTrue(is_ascii(u"`1234567890-=`"))
        self.assertTrue(is_ascii(u"~!@#$%^&*()_+"))
        self.assertTrue(is_ascii(u"[]\\;',./}{|:<>?"))
        self.assertFalse(is_ascii(u"·"))
        self.assertFalse(is_ascii(u"～"))
        self.assertFalse(is_ascii(u"！"))
        self.assertFalse(is_ascii(u"。"))
        self.assertFalse(is_ascii(u"，"))
        self.assertFalse(is_ascii(u"测试"))


if __name__ == "__main__":
    unittest.main()
