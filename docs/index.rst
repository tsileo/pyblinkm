.. PyBlinkM documentation master file, created by
   sphinx-quickstart on Thu Jan 24 13:16:35 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyBlinkM's documentation!
====================================

Drive a `BlinkM <http://thingm.com/products/blinkm>`_ with **Python** via I2C using python-smbus on `Raspberry Pi <http://www.raspberrypi.org/>`_.

::

    $ sudo apt-get install python-smbus
    $ sudo pip install pyblinkm
    $ python
    >>> from pyblinkm import BlinkM, Scripts
    >>> blinkm = BlinkM()
    >>> blinkm.reset()
    >>> blinkm.play_script(Scripts.THUNDERSTORM)
    >>> blinkm.reset()
    >>> blinkm.fade_to(255, 0, 0)
    >>> blinkm.fade_to_hex("ff0000")
    >>> blinkm.go_to(0, 255, 0)

Contents:

.. automodule:: pyblinkm
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

