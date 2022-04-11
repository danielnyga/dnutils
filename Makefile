
all:
	echo "Running all tests..."
	rm -rf tmpenv-dnutils-`cat version` && virtualenv tmpenv-dnutils-`cat version` && . tmpenv-dnutils-`cat version`/bin/activate && pip install -r requirements.txt && cd test && echo `python --version` && export PYTHONPATH=../src && python -m unittest discover -s `pwd` -t `pwd` && cd .. && rm -r tmpenv-dnutils-`cat version`
	echo "Build dnutils package..."
	python setup.py sdist
	rm -rf tmpenv-dnutils-`cat version` && virtualenv tmpenv-dnutils-`cat version` && . tmpenv-dnutils-`cat version`/bin/activate && pip install dist/dnutils-`cat version`.tar.gz && echo `python -c "from dnutils.version import VERSION_STRING_FULL; print('dnutils version %s build successful.' % VERSION_STRING_FULL)"` && rm -r tmpenv-dnutils-`cat version`

upload:
	twine upload dist/dnutils-`cat version`.tar.gz

clean:
	rm -rf dist *.egg-info *.log .dnutils tmpenv-dnutils-*