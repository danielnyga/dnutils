General Purpose Tools
---------------------

.. autofunction:: dnutils.tools.ifnone

.. autofunction:: dnutils.tools.ifnot

.. autofunction:: dnutils.tools.allnone

.. autofunction:: dnutils.tools.allnot

.. autofunction:: dnutils.tools.ifstr

.. autofunction:: dnutils.tools.isnone

.. autofunction:: dnutils.tools.is_not_none

.. autofunction:: dnutils.tools.where

.. autofunction:: dnutils.tools.where_not


List Convenience Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dnutils.tools.idxif

.. autofunction:: dnutils.tools.first

.. autofunction:: dnutils.tools.last

.. autofunction:: dnutils.tools.mapstr

.. autofunction:: dnutils.tools.chunks

.. autofunction:: dnutils.tools.pairwise

.. autofunction:: dnutils.tools.project

.. autofunction:: dnutils.tools.allin

.. autofunction:: dnutils.tools.allequal

Other Tools
~~~~~~~~~~~

.. autofunction:: dnutils.tools.LinearScale

.. autofunction:: dnutils.tools.str2bool


Enhanced Dictionary Functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Multiple Signal Handlers
~~~~~~~~~~~~~~~~~~~~~~~~

The original :mod:`signal` module only allows to register one handler 
at a time. :mod:`dnutils.signals` can be used to register an arbitrary 
number of different handlers, which will all be executed in the order 
they have been registered. More information can be found on
:doc:`signals`.


.. .. toctree::
   :hidden:
   debug
   console
   threads
   logging
