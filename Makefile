EXTRA_REQUIREMENTS=pymongo mongomock numpy

all:
	echo "Running all tests..."
	rm -r tmpenv-dnutils-`cat version` || virtualenv tmpenv-dnutils-`cat version` && . tmpenv-dnutils-`cat version`/bin/activate && pip install -r requirements.txt && pip install ${EXTRA_REQUIREMENTS} && cd test && echo `python --version` && export PYTHONPATH=../src && python -m unittest discover -s `pwd` -t `pwd` && cd .. && rm -r tmpenv-dnutils-`cat version`
	echo "Build dnutils package..."
	python setup.py sdist
	rm -r tmpenv-dnutils-`cat version` || virtualenv tmpenv-dnutils-`cat version` && . tmpenv-dnutils-`cat version`/bin/activate && pip install dist/dnutils-`cat version`.tar.gz && pip install ${EXTRA_REQUIREMENTS} &&  echo `python -c "from dnutils.version import VERSION_STRING_FULL; print('dnutils version %s build and test successful.' % VERSION_STRING_FULL)"` && rm -r tmpenv-dnutils-`cat version`

deployment:
	twine upload dist/dnutils-`cat version`.tar.gz

clean:
	rm -rf dist *.egg-info *.log .dnutils tmpenv-dnutils-*