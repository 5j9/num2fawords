cd ..
echo Creating a Source Distribution:
python setup.py sdist
echo Creating a Pure Python Wheel:
python setup.py bdist_wheel
echo All done!
read
