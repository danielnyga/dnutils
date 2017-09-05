.. dnutils documentation master file, created by
   sphinx-quickstart on Mon May 22 15:10:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to dnutils' documentation!
==================================

`dnutils` is a collection of convenience functions, tools and classes 
for situations I find myself very frequently. I have developed this 
toolbox with the goal to provide a practical, easy-to-use and 
well-documented collection of utilities for debugging, console output,
data structures.

Installation
~~~~~~~~~~~~

Using ``pip``:

.. code-block:: bash

   $ pip install dnutils

Get the source code from: ::

   https://github.com/danielnyga/dnutils

The repository contains the branches ``python2.7`` and ``python3.5`` which hold implementations of `dnutils`
in the respective Python version. The ``master`` branch is a meta-checkout containing both ``python2.7`` and
``python3.5`` as submodules. It also holds the release tags and ``setup.py``. After cloning it with::

   git clone --recursive https://github.com/danielnyga/dnutils

one should have the following directory structure:::

   ./python3.5
   ./python2.7
   ./_version
   ./doc
   ./test.py
   ./setup.py
   ./setup.cfg
   ./LICENSE
   ./MANIFEST.in
   ./README.md
   ./.gitmodules
   ./.gitignore


.. toctree::
   :hidden:

   tools
   debug
   console
   threads
   logging
   signals
   stats
