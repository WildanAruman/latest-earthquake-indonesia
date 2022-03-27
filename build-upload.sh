#! /bin/sh
rm -r dist
python -m build
python -m twine upload --repository pypi dist/*