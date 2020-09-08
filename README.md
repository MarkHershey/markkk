# Python Package: markkk

Convenient Python utilities for personal usage


## Install

```bash
pip install --upgrade markkk
```

## Usage

### Generic Colored Logger

This is a pre-configured logger using python's built-in `logging` module and a formatter [`colorlog`](https://github.com/borntyping/python-colorlog). It is easy to use, simplest setup on earth, suitable for personal day-to-day debugging, personal small-scale projects.

```python
from markkk.logger import logger

logger.debug("This is a debug message")
logger.info("This is a message for your information")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical error message")

```

The logger has three logging handlers:
1. log to file `logs/debug.log` which captures all logs with timestamp.
2. log to file `logs/error.log` which captures error & critical logs with timestamp.
3. log to console with colors for different logging levels.


### Sub-module: `check_text_encoding`

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
cd markkk
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
