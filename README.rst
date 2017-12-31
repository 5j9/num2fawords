.. image:: https://travis-ci.org/5j9/num2fawords.svg?branch=master
	:target: https://travis-ci.org/5j9/num2fawords
.. image:: https://codecov.io/github/5j9/num2fawords/coverage.svg?branch=master
	:target: https://codecov.io/github/5j9/num2fawords
.. image:: https://ci.appveyor.com/api/projects/status/github/5j9/num2fawords?svg=true&branch=master
	:target: https://ci.appveyor.com/project/5j9/num2fawords

num2fawords
===========

`num2fawords` is a highly customizable library which provides functions to convert a number (int, float, Decimal, Fraction, or str) into Persian word form.

Installation
============

- Python 3.3+ is required
- ``pip install 'setuptools>=36.2.1'``
- ``pip install num2fawords``

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
	>>> words(1.1e-9)
	'یک و یک دهم در ده به توان منفی نه'


Obviously, `words` is used to convert to word form and `ordinal_words` is for ordinal word from.

`words` also accepts other common standard types:

.. code-block:: python

	>>> words(19.75)
	'نوزده و هفتاد و پنج صدم'
	>>> from decimal import Decimal
	>>> words(Decimal('1.1'))
	'یک و یک دهم'
	>>> from fractions import Fraction
	>>> words(Fraction(-2, 5))
	'منفی دو پنجم'


The default decimal separator is "و" but it can be changed to "ممیز" (or any other string) as follows:

.. code-block:: python

	>>> words(19.75, decimal_separator=' ممیز ')
	'نوزده ممیز هفتاد و پنج صدم'

Some people prefer, for example, "صد و هفتاد" over its other form "یکصد و هفتاد". This library uses the second form by default which is also used on official Iranian banknotes. But it can be changed:

.. code-block:: python

	>>> from num2fawords import HUNDREDS
	>>> words(170)
	'یکصد و هفتاد'
	>>> HUNDREDS[1] = 'صد'
	>>> words(170)
	'صد و هفتاد'

Some examples for other arguments of `words`:

.. code-block:: python

	>>> words(7, positive='مثبت ')
	'مثبت هفت'
	>>> words(-2, negative='منهای ')
	'منهای دو'
	>>> words('۱/۲')
	'یک دوم'
	>>> words('1/2', fraction_separator=' تقسیم بر ', ordinal_denominator=False)
	'یک تقسیم بر دو'
	>>> words(1.1e-9)
	'یک و یک دهم در ده به توان منفی نه'
	>>> words(1.1e-9, scientific_separator=' ضربدر ده به قوهٔ ')
	'یک و یک دهم ضربدر ده به قوهٔ منفی نه'

Of-course the above arguments can be used together.

If you prefer to change the default argument values once and for all, use the `change_defaults` function:

.. code-block:: python

	>>> from num2fawords import change_defaults, words
	>>> change_defaults(fraction_separator=' بخش بر ', ordinal_denominator=False)
	>>> words('۱/۴')
	'یک بخش بر چهار'

That's all. Enjoy!
