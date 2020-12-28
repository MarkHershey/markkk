# Release a Python Package

1. Register for a PyPi account
2. Generate a PyPi token
3. Build
```
check-manifest --create
```
```
python setup.py sdist bdist_wheel
```
4. Install `twine`
```
pip install twine
```

5. Upload to PyPi
```
python -m twine upload dist/*
```
