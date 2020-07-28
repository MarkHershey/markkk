# markkk

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
from markkk.pyutils import *

replace_punc_for_file("test.txt")
is_ascii("。") # this returns false
```



## Development

### Install package using local version
*clone this repo*
```bash
git clone https://github.com/MarkHershey/python-utils.git
```
*go to project root*
```bash
cd python-utils
```

*create virtual env for this project*
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools  wheel
pip install -r requirements.txt
```

*install this package in editable mode*
```bash
pip install -e .[dev]
```

### Run Unittest

*at project root*
```bash
tox
```

## License

- [MIT License]("LICENSE")
