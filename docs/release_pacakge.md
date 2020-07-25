# Release a Python Package

1. Register for a PyPi account
2. Generate a PyPi token
3. Build
```
python setup.py sdist bdist_wheel
```
4. Install `twine`
```
pip install twine
```
4. Upload
```
python -m twine upload dist/*
```
