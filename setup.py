import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'dnutils', 'VERSION'), 'r') as f:
    __version__ = f.read().strip()

setup(
    name = 'dnutils',
    packages = ['dnutils'],
    version = __version__,
    description = 'A collection of convenience tools for everyday Python programming',
    author = 'Daniel Nyga',
    author_email = 'daniel.nyga@t-online.de',
    url = 'https://spritinio.de/dnutils',
    download_url = 'https://github.com/danielnyga/dnutils/archive/%s.tar.gz' % __version__,
    keywords = ['testing', 'logging', 'threading', 'multithreading', 'debugging', 'tools'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
        'Topic :: Utilities'

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'colored==1.3.5',
        'tabulate',
        'portalocker',
    ],
    package_data={
        '': [
            'VERSION',
        ]
    },
)