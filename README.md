# `markkk`

Convenient Python utilities for personal usage

## Install

```bash
pip install markkk
```

## Usage

### sub-module: check_text_encoding

- `is_ascii`
- `check_non_ascii_index`
- `is_ascii_only_file`
- `check_file_by_line`
- `ensure_no_zh_punctuation`
- `replace_punc_for_file`

*Example*:

```python
import markkk.pyutils as utils

utils.replace_punc_for_file("test.txt")
```

## License

- MIT
