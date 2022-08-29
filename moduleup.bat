@echo off
color 3
title Lool xdd
echo Building the next version
echo Ok, building version
title Lool xd - Building version
python setup.py sdist bdist_wheel
title xdd Done
cls
echo Ok, taht is done. (Not a gramer mistake xed)
color 5
title Loooox xdd - Uploading module
echo Uploading module
twine upload --skip-existing dist/*