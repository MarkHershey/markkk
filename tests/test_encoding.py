import sys
import unittest
from pathlib import Path

project_root_dir = Path(__file__).resolve().parent.parent
src_dir = project_root_dir / "src/markkk"
res_dir = project_root_dir / "tests/resources"

sys.path.insert(0, str(src_dir))

from encoding import (
    check_file_by_line,
    check_non_ascii_char,
    check_non_ascii_index,
    ensure_no_zh_punctuation,
    is_ascii,
    is_ascii_only_file,
    replace_punc_for_file,
)


class TestEncoding(unittest.TestCase):
    def test_check_file_by_line(self):
        test_fp = res_dir / "test.txt"
        check_file_by_line(test_fp)

    def test_check_non_ascii_char(self):
        result = check_non_ascii_char("fjashdfisahdfoisafieiowhfioash")
        self.assertEqual(result, None)
        result = check_non_ascii_char("123456789。")
        self.assertTrue(isinstance(result, tuple))

    def test_is_ascii(self):
        with self.assertRaises(Exception):
            is_ascii(100)

    def test_check_non_ascii_index(self):
        with self.assertRaises(TypeError):
            check_non_ascii_index(100)

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

    def test_is_ascii_only_file(self):
        test_fp = res_dir / "test.txt"
        self.assertFalse(is_ascii_only_file(test_fp))

    def test_replace_punc_for_file(self):
        test_fp = res_dir / "test.txt"
        new_fp = replace_punc_for_file(test_fp)
        self.assertTrue(is_ascii_only_file(new_fp))


if __name__ == "__main__":
    unittest.main()
