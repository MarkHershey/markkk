import os
from pathlib import Path
from typing import List, Tuple


def is_ascii(text: str) -> bool:
    """ Check if a string contains ascii character only. """
    if isinstance(text, str):
        try:
            text.encode("ascii")
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode("ascii")
        except UnicodeDecodeError:
            return False
    return True


def check_non_ascii_index(string: str) -> Tuple[int]:
    if not isinstance(string, str):
        # print(f"{type(string)} is not string.")
        raise TypeError(f"{type(string)} is not string.")

    if is_ascii(string):
        return None

    index_list: List[str] = []

    for index, char in enumerate(string):
        if ord(char) >= 128:
            index_list.append(index + 1)

    return tuple(index_list)


def check_non_ascii_char(string: str) -> Tuple[str]:
    if not isinstance(string, str):
        # print(f"{type(string)} is not string.")
        raise TypeError(f"{type(string)} is not string.")

    if is_ascii(string):
        return None

    index_list = []

    for index, char in enumerate(string):
        if ord(char) >= 128:
            index_list.append(f"{index + 1}: {char}")

    return tuple(index_list)


def is_ascii_only_file(filepath: str) -> bool:
    """ Check if a file contains ascii character only. """
    filepath = Path(filepath)
    assert filepath.is_file()

    with filepath.open(encoding="utf-8") as f:
        text = f.read()

    return is_ascii(text)


def check_file_by_line(filepath: str) -> None:
    filepath = Path(filepath)
    assert filepath.is_file()

    if is_ascii_only_file(filepath):
        print("OK")
        return
    else:
        print("\nFollowing lines contain non-ascii characters:\n")

    with filepath.open(encoding="utf-8") as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        line_number = index + 1
        if not is_ascii(line):
            print(f"{line_number}: {check_non_ascii_char(line)}")

    print("---END---\n")


def ensure_no_zh_punctuation(string: str) -> str:
    """Convert common Chinese (zh) punctuation (Unicode) to
    corresponding English (en-us) punctuation (ascii).
    """
    if not isinstance(string, str):
        print(f"{type(string)} is not string.")

    if is_ascii(string):
        return string

    punc_map = {
        "。": ".",
        "，": ",",
        "、": ",",
        "？": "?",
        "！": "!",
        "；": ";",
        "：": ":",
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "【": "[",
        "】": "]",
        "「": "{",
        "」": "}",
        "｜": "|",
        "—": "-",  # ord = 8212
        "（": "(",
        "）": ")",
        "～": "~",
        "《": "<",
        "》": ">",
        "……": "...",
        "…": "...",
        "·": "-",
        "¥": "$",
    }
    new_string = ""
    for char in string:
        # print(f"{char}: {ord(char) if ord(char) >= 128 else '>>>ascii'}")
        new_string += punc_map.get(char, char)
    return new_string


def replace_punc_for_file(filepath: str) -> Path:
    filepath = Path(filepath)
    assert filepath.is_file()
    filepath = filepath.resolve()

    head, tail = os.path.split(filepath)
    name, ext = os.path.splitext(tail)

    with filepath.open(encoding="utf-8") as f:
        content = f.read()

    content_new = ensure_no_zh_punctuation(content)
    filepath_new = Path(head) / f"{name}_new{ext}"

    with filepath_new.open(mode="w", encoding="utf-8") as f:
        f.write(content_new)
        print(f"Successfully exported: {filepath_new}")

    return filepath_new


if __name__ == "__main__":
    # ensure_no_zh_punctuation("哈水淀粉和卡积分")
    # ensure_no_zh_punctuation("，。？！#¥%……&*（）——-=+【】「」；‘：“《》/”’")
    replace_punc_for_file("test.txt")
