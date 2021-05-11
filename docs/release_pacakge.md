# Release a Python Package

1. Register for a PyPi account
2. Generate a PyPi token
3. Build

```bash
check-manifest --create
```

```bash
python setup.py sdist bdist_wheel
```

4. Install `twine`

```bash
pip install twine
```

5. Upload to PyPi

```bash
python -m twine upload dist/*
```
