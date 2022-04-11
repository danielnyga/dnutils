PKG_NAME=dnutils
PKG_VERSION=`cat version`
ENV_NAME=tmpenv-${PKG_NAME}-${PKG_VERSION}

all:
	echo "Running all tests..."
	rm -rf ${ENV_NAME} && virtualenv ${ENV_NAME} && . ${ENV_NAME}/bin/activate && pip install -r requirements.txt && cd test && echo `python --version` && export PYTHONPATH=../src && python -m unittest discover -s `pwd` -t `pwd` && cd .. && rm -r ${ENV_NAME}
	echo "Build dnutils package..."
	python setup.py sdist
	rm -rf ${ENV_NAME} && virtualenv ${ENV_NAME} && . ${ENV_NAME}/bin/activate && pip install dist/${PKG_NAME}-${PKG_VERSION}.tar.gz && echo `python -c "from ${PKG_NAME}.version import VERSION_STRING_FULL; print('${PKG_NAME} version %s build successful.' % VERSION_STRING_FULL)"` && rm -r ${ENV_NAME}

upload:
	twine upload dist/${PKG_NAME}-${PKG_VERION}.tar.gz

clean:
	rm -rf dist *.egg-info *.log tmpenv-${PKG_NAME}
