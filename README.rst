.. dnutils documentation master file, created by
   sphinx-quickstart on Mon May 22 15:10:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to dnutils's documentation!
===================================

`dnutils` is a collection of convenience functions, tools and classes 
for situations I find myself very frequently. I have developed this 
toolbox with the goal to provide a practical, easy-to-use and 
well-documented collection of utilities for debugging, console output
and data structures.

Debugging
---------

The :mod:`dnutils.debug` module provides a couple of useful tools
for convenient and lightweight debugging.

Printing
~~~~~~~~

The first and simplest function is the :func:`out` function:

.. autofunction:: dnutils.debug.out

The :func:`out` function is a simple wrapper around Python's ordinary
:func:`print` function, but it prepends to any output the module's file
name and line number of the calling frame. Let us consider an exemplay 
python module ``test.py``: 

.. code-block:: python
   :linenos:
   
   from dnutils import out

   if __name__ == '__main__':
       out('hello, world!')

Running the module prints ::

   $ python test.py
   test.py: l.4: hello, world!
   
So, :func:`dnutils.debug.out` is basically a print function that allows
to trace back where the call to it was actually issued. 

Ideally, one should set up a real logging infrastructure
properly instead of using ``print``. However, the :func:`out`
function provides a convenient way of doing it the "quick-and-dirty" 
way, which lets one locate the print statements that one has introduced 
in the code, which can be really cumbersome to detect.

The :func:`out` function has a parameter ``tb`` that extends the 
parameter list inherited from :func:`print`. Normally, when just 
printing single statements to the console, one can just disregard it. 
However, it might happen that one wants to outsource a more complex 
debug output into a separate function. For example, consider the 
following function that prints all global variables in the current 
frame: 

.. code-block:: python
   :linenos:
   
   def print_globals():
       out('global variables'):
       for k, v in globals().iter():
           print(k, ': ', v)
           
If the :func:`print_globals` function is now used somewhere in the 
code, the location printed would always be the :func:`out` call (in 
this example, line 2). The desirable output, however, would be the 
location of the :func:`print_globals` function. The :func:`out` 
function provides an additional parameter ``tb``, which lets us control 
the number of indirections that it traces back to find the actual 
caller frame. As :func:`out` is used in one additional level of 
indirections, 

.. code-block:: python
   :linenos:
   
   def print_globals():
       out('global variables', tb=2):
       for k, v in globals().iter():
           print(k, ': ', v)

Always prints the desired location in the code, where 
:func:`print_globals` is called.

The :func:`dnutils.debug.stop` function is a modification of 
:func:`dnutils.debug.out`, which stops after having printed the 
desired output and waits until the user presses the return key:

.. autofunction:: dnutils.debug.stop

.. code-block:: python
    
   >>> from dnutils import stop
   >>> stop('waiting...')
   <stdin>: l.1: waiting...
   <press enter to continue> # hit enter here
   >>> 
    


Stack Traces
~~~~~~~~~~~~

.. autofunction:: dnutils.debug.trace

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Tools
-----

The :func:`dnutils.tools.ifnone` function is supposed to make the 
ternary Python ``if-then-else`` idiom less verbose. The basic idea 
of this function is that in many cases one is supposed to do only
little operations on a variable ``x``, but only if ``x`` is not ``None``. 
A popular case is, for example, to obtain a string representation of ``x``, 
but some special treatment of the ``None`` case: ::

    >>> str(x) if x is not None else 'N/A'
    
So far, so good. As long as ``x`` is a pretty short expression, there is 
nothing to argue against the above construct. But what if ``x`` is, for 
instance, a concatenation of functions or dictionary queries, like ::

    >>> str(myobj.textfield.gettext().getdata()) if myobj.textfield.gettext().getdata() is not None else ''
    
There are at least three shortcomings with such a construct:

  * Verbosity: myobj.textfield.gettext().getdata() needs to be written twice
  * Speed: myobj.textfield.gettext().getdata() needs to be evaluated twice
  * Readability: the expression is hard to read

To make such constructs more convenient, `dnutils` provide the 
:func:`dnutils.tools.ifnone` function:
  
.. autofunction:: dnutils.tools.ifnone

Using :func:`dnutils.tools.ifnone`, the above expression can be written
more concisely as ::

    >>> ifnone(myobj.textfield.gettext().getdata(), '', str)
    
Another frequent example is parsing a number with a default value in
case of ``None``: ::

    ifnone(str_to_parse, 0, int)
    
.. note::
    Note that, in contrast to the ternary ``if-then-else`` construct,
    :func:`dnutils.tools.ifnone` always evaluates the ``else`` part, i.e.
    it does not support lazy evaluation.
    
:func:`dnutils.tools.ifnot` is equivalent to :func:`ifnone` except
for it checks for Boolean truth instead of ``None``:
    
.. autofunction:: dnutils.tools.ifnot 

.. autofunction:: dnutils.tools.allnone

.. autofunction:: dnutils.tools.allnot

Console
-------

Progress Bars
~~~~~~~~~~~~~

.. autoclass:: dnutils.console.ProgressBar
    :members: __init__, setlayout, update, inc, finish

Status Messages
~~~~~~~~~~~~~~~

`dnutils` contains a class that mimics the behavior of
status messages of a typical Linux boot screen:

.. image:: _static/status-msg.png


.. autoclass:: dnutils.console.StatusMsg
    :members: __init__, setwidth, write, finish

A :class:`dnutils.console.StatusMsg` object can be instantiated
with an optional width, a message and a status. The width is a
string or a number determining the width (in absolute characters)
or the percentage of console that the status message will consume.
A behavior as shown in the above screenshot, for instance, can be
achieved by somehting like::

    for i in range(100):
        status = StatusMsg(message='  * Operation #%d:' % (i + 1))
        status.status = StatusMsg.OK if random.random() > .3 else StatusMsg.ERROR
        status.finish()

which will print 100 status bars and assign each the status ``OK``
with 70% probability and an ``ERROR`` state with 30%. The
following predefined stati are available:

* :attr:`dnutils.console.StatusMsg.OK` - a green "OK" label
* :attr:`dnutils.console.StatusMsg.ERROR` - a red "ERROR" label
* :attr:`dnutils.console.StatusMsg.PASSED` - a green "PASSED" label
* :attr:`dnutils.console.StatusMsg.FAILED` - a red "FAILED" label
* :attr:`dnutils.console.StatusMsg.WARNING` - a yellow "WARNING" label

For a particular ``StatusMsg`` instance, the set of available
stati can be customized by handing them over in the ``stati``
parameter of the constructor. A status is just a (possibly ASCII
escaped color) string. So customized status labels can be
easily created.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
