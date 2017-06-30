.. image:: https://travis-ci.org/5j9/num2fawords.svg?branch=master
	:target: https://travis-ci.org/5j9/num2fawords
.. image:: https://codecov.io/github/5j9/num2fawords/coverage.svg?branch=master
	:target: https://codecov.io/github/5j9/num2fawords

num2fawords
===========

This package provides functions to convert a number (int or float) to a Persian
word form.

installation
============

Python 3.3+ is required.

Install using `pip install num2fawords` command.

Usage
=====

.. code-block:: python

	>>> from num2fawords import words, ordinal_words
	>>> words(1984)
	'یک هزار و نهصد و هشتاد و چهار'
	>>> ordinal_words(1232)
	'یک هزار و دویست و سی و دوم'
	>>> ordinal_words(123)
	'یکصد و بیست و سوم'

Obviously, `words` is used convert to word form and `ordinal_words` is for ordinal word from.

Use can also pass in floating point numbers:

.. code-block:: python

	>>> words(19.75)
	'نوزده و هفتاد و پنج صدم'

This is the default setting. If you'd like to use "ممیز" instead of "و" for decimal point, you can:

.. code-block:: python

	>>> import num2fawords
	>>> num2fawords.DECIMAL_SEPARATOR  # default value:
	' و '
	>>> num2fawords.DECIMAL_SEPARATOR = ' ممیز '
	>>> words(19.75)
	'نوزده ممیز هفتاد و پنج صدم'

Also some people prefer, for example, "صد و هفتاد" over its other form "یکصد و هفتاد". This library uses the second form which is the form used on official Iranian banknotes. But it can be changed:

.. code-block:: python

	>>> from num2fawords import HUNDREDS
	>>> words(170)
	'یکصد و هفتاد'
	>>> HUNDREDS[1] = 'صد'
	>>> words(170)
	'صد و هفتاد'
