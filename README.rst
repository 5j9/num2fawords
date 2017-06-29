number2farsiword
================

This package provides functions to convert a number (int or float) to a Persian
word form.

Usage
=====

.. code-block:: python

	>>> from number2farsiword import cardinal_words, ordinal_words
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
	'نوزده ممیز هفتاد و پنج صدم'

This is the default setting. If you'd like to ommit the word "ممیز" from the output and use "و" instead of it, you can:

.. code-block:: python

	>>> import number2farsiword
	>>> number2farsiword.MOMAYEZ  # default value:
	' ممیز '
	>>> number2farsiword.MOMAYEZ = ' و '
	>>> number2farsiword.cardinal_words(19.75)
	'نوزده و هفتاد و پنج صدم'

Also some people prefer, for example, "صد و هفتاد" over its other form "یکصد و هفتاد". This library uses the second form which is the form used on official Iranian banknotes. But it can be changed:

.. code-block:: python

	>>> number2farsiword.cardinal_words(170)
	'یکصد و هفتاد'
	>>> number2farsiword.SADGAN
	['', 'یکصد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد']
	>>> number2farsiword.SADGAN[1] = 'صد'
	>>> number2farsiword.cardinal_words(170)
	'صد و هفتاد'

Command line
============

The program can also be invoked from the command line:

.. code-block::

	>python number2farsiword.py
	usage: number2farsiword.py [-h] [--ordinal] [--cardinal] number
	number2farsiword.py: error: the following arguments are required: number
	>python number2farsiword.py 13
	سیزدهم
	>python number2farsiword.py -o 13
	سیزدهم
