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

	>>> from num2fawords import cardinal_words, ordinal_words
	>>> cardinal_words(1984)
	'یک هزار و نهصد و هشتاد و چهار'
	>>> ordinal_words(1232)
	'یک هزار و دویست و سی و دوم'
	>>> ordinal_words(123)
	'یکصد و بیست و سوم'

Obviously, `cardinal_words` is used convert to cardinal form and `ordinal_words` for ordinal from.

Use can also pass in floating point numbers:

.. code-block:: python

	>>> cardinal_words(19.75)
	'نوزده و هفتاد و پنج صدم'

This is the default setting. If you'd like to use "ممیز" instead of "و" for decimal point, you can:

.. code-block:: python

	>>> from num2fawords import DECIMAL_SEPARATOR
	>>> DECIMAL_SEPARATOR  # default value:
	' و '
	>>> DECIMAL_SEPARATOR = ' ممیز '
	>>> cardinal_words(19.75)
	'نوزده ممیز هفتاد و پنج صدم'

Also some people prefer, for example, "صد و هفتاد" over its other form "یکصد و هفتاد". This library uses the second form which is the form used on official Iranian banknotes. But it can be changed:

.. code-block:: python

	>>> from num2fawords import HUNDREDS
	>>> cardinal_words(170)
	'یکصد و هفتاد'
	>>> HUNDREDS[1] = 'صد'
	>>> cardinal_words(170)
	'صد و هفتاد'
