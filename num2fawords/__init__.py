"""Provide functions to convert a number (int) to Persian words."""

from decimal import Decimal
from fractions import Fraction
from itertools import chain as _chain
try:
    from functools import singledispatch as _singledispatch
except ImportError:
    # sys.version_info < (3, 4)
    # noinspection PyUnresolvedReferences
    from singledispatch import singledispatch as _singledispatch
from typing import Union as _Union


ONES = [
    '',
    'یک',
    'دو',
    'سه',
    'چهار',
    'پنج',
    'شش',
    'هفت',
    'هشت',
    'نه',
]

TENS = [
    '',
    '',
    'بیست',
    'سی',
    'چهل',
    'پنجاه',
    'شصت',
    'هفتاد',
    'هشتاد',
    'نود',
]

TEN_TO_TWENTY = [
    'ده',
    'یازده',
    'دوازده',
    'سیزده',
    'چهارده',
    'پانزده',
    'شانزده',
    'هفده',
    'هجده',
    'نوزده',
]

HUNDREDS = [
    '',
    'یکصد',
    'دویست',
    'سیصد',
    'چهارصد',
    'پانصد',
    'ششصد',
    'هفتصد',
    'هشتصد',
    'نهصد',
]

CLASSES = [
    '',
    ' هزار',
    ' میلیون',
    ' میلیارد',
    ' بیلیون',
    ' بیلیارد',
    ' تریلیون',
    ' ترلیارد',
    ' کوآدریلیون',
    ' کادریلیارد',
    ' کوینتیلیون',
    ' کوانتینیارد',
]

DECIMAL_PLACES = ['', ' دهم', ' صدم']
DECIMAL_PLACES.extend(_chain.from_iterable(
    (i, ' ده' + i, ' صد' + i)
    for i in (i + 'م' for i in CLASSES[1:])
))

_NORMALIZATION_TABLE = str.maketrans('E٫', 'e.', '_٬,')


def _three_digit_words(threedigit: str) -> str:
    """Return the word representation of threedigit."""
    h, t, o = threedigit
    if h == '0' or threedigit[1:] == '00':
        w = HUNDREDS[int(h)]
    else:
        w = HUNDREDS[int(h)] + ' و '
    if t == '1':
        return w + TEN_TO_TWENTY[int(o)]
    if o == '0' or t == '0':
        w += TENS[int(t)]
    else:
        w += TENS[int(t)] + ' و '
    return w + ONES[int(o)]


# noinspection PyUnusedLocal
@_singledispatch
def words(
    number: _Union[int, float, str, Decimal],
    plus: str='',
    minus: str='منفی ',
    decimal_separator: str=' و ',
    fraction_separator: str=' و ',
    ordinal_denominator: str=' و ',
) -> str:
    raise TypeError('invalid input type for words function', number)


@words.register(str)
def _(
    number: _Union[int, float, str, Decimal],
    plus: str='',
    minus: str='منفی ',
    decimal_separator: str=' و ',
    fraction_separator: str=' و ',
    ordinal_denominator: str=' و ',
) -> str:
    """Return the word form of number."""
    # Normalize the str
    number = str(number).strip().translate(_NORMALIZATION_TABLE)

    # sign
    c0 = number[0]
    if c0 == '-':
        sign = minus
        number = number[1:]
    elif c0 == '+':
        sign = plus
        number = number[1:]
    else:
        sign = ''

    nominator, e, denominator = number.partition('/')

    if denominator:
        if ordinal_denominator:
            return (
                sign
                + _no_fraction_words(nominator, decimal_separator)
                + fraction_separator
                + ordinal_words(denominator)
            )
        return (
            sign
            + _no_fraction_words(nominator, decimal_separator)
            + fraction_separator
            + _no_fraction_words(denominator, decimal_separator)
        )
    return sign + _no_fraction_words(nominator, decimal_separator)


# noinspection PyUnusedLocal
@words.register(Decimal)
def _(
    number: Decimal,
    plus: str = '',
    minus: str = 'منفی ',
    decimal_separator: str = ' و ',
    fraction_separator: str = ' و ',
    ordinal_denominator: str = ' و ',
) -> str:
    return words.registry[str](
        str(number),
        plus,
        minus,
        decimal_separator,
        fraction_separator,
        ordinal_denominator,
    )


# noinspection PyUnusedLocal
@words.register(int)
def _(
    number: int,
    plus: str = '',
    minus: str = 'منفی ',
    decimal_separator: str = ' و ',
    fraction_separator: str = ' و ',
    ordinal_denominator: str = ' و ',
) -> str:
    """Return the fa-word form for the given int."""
    if number == 0:
        return 'صفر'
    if number < 0:
        return minus + _natural_words(str(number)[1:])
    return _natural_words(str(number))


# noinspection PyUnusedLocal
@words.register(float)
def _(
    number: float,
    plus: str = '',
    minus: str = 'منفی ',
    decimal_separator: str = ' و ',
    fraction_separator: str = ' و ',
    ordinal_denominator: str = ' و ',
) -> str:
    """Return the fa-word form for the given float."""
    if number == 0:
        return 'صفر'
    str_num = str(number)
    if number < 0:
        return _no_fraction_words(str_num[1:], decimal_separator)
    return _no_fraction_words(str_num, decimal_separator)


def _no_fraction_words(
    number: str,
    decimal_separator: str,
) -> str:
    # exponent
    base, e, exponent = number.partition('e')
    if exponent:
        return (
            _no_exponent_words(base, decimal_separator)
            + ' ضربدر ده به توان '
            + words(exponent, decimal_separator)
        )
    return _no_exponent_words(base, decimal_separator)


def _no_exponent_words(
    number: str,
    decimal_separator: str,
) -> str:
    before_p, p, after_p = number.partition('.')
    if after_p:
        if before_p == '0':
            if after_p == '0':
                return 'صفر'
            return _natural_words(after_p) + DECIMAL_PLACES[len(after_p)]
        if after_p != '0':
            return (
                _natural_words(before_p)
                + decimal_separator
                + _natural_words(after_p)
                + DECIMAL_PLACES[len(after_p)]
            )
        return _natural_words(before_p)
    return _natural_words(before_p)


def _natural_words(number: str) -> str:
    if number == '0':
        return 'صفر'
    length = len(number)
    if length > len(CLASSES) * 3:
        raise ValueError('out of range')

    modulo_3 = length % 3
    if modulo_3:
        number = '0' * (3 - modulo_3) + number
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    natural_words = ''
    while group > 0:
        three_digit = number[group * 3 - 3:group * 3]
        word3 = _three_digit_words(three_digit)
        if word3 and group != groups:
            if natural_words:
                natural_words = word3 + CLASSES[groups - group] + \
                                ' و ' + natural_words
            else:
                natural_words = word3 + CLASSES[groups - group]
        else:
            natural_words = word3 + natural_words
        group -= 1

    return natural_words


def ordinal_words(number: _Union[int, str])-> str:
    """Return the ordinal_words form of the number converted to words."""
    w = words(number)
    if w[-2:] == 'سه':
        return w[:-2] + 'سوم'
    return w + 'م'
