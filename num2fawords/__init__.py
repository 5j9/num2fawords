"""Provide functions to convert a number (int) to Persian words."""

try:
    from functools import singledispatch as _singledispatch
except ImportError:
    # sys.version_info < (3, 4)
    # noinspection PyUnresolvedReferences
    from singledispatch import singledispatch as _singledispatch
from typing import Union as _Union
from itertools import chain as _chain


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

DECIMAL_SEPARATOR = ' و '


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


@_singledispatch
def words(number: _Union[int, float, str]) -> str:
    """Return the word form of number."""
    # Todo: Add support for fractions (fractions.Fraction)
    # Unregistered type (str, Decimal, etc.)
    try:
        return words.registry[int](int(number))
    except ValueError:
            return words.registry[float](float(number))


@words.register(int)
def _(number: int) -> str:
    if number == 0:
        return 'صفر'
    if number < 0:
        return'منفی ' + _natural_words(str(number)[1:])
    else:
        return _natural_words(str(number))


@words.register(float)
def _(number: float) -> str:
    """Return the fa-word form for the given float."""
    if number == 0:
        return 'صفر'

    str_num = str(number)
    if number < 0:
        str_num = str_num[1:]
        negative = 'منفی '
    else:
        negative = ''

    base, e_, exponent = str_num.rpartition('e-')

    if e_:
        # Todo: Can the exponent be out of DECIMAL_PLACES range? If yes,
        # raise ValueError.
        if base[1:2] == '.':
            return _natural_words(base[:1] + base[2:]) + \
                   DECIMAL_PLACES[int(exponent) + len(base) - 2]
        else:
            return _natural_words(base) + \
                   DECIMAL_PLACES[int(exponent)]

    str_int, _, str_dec = str_num.rpartition('.')
    if str_int == '0':
        return _natural_words(str_dec) + DECIMAL_PLACES[len(str_dec)]
    if str_dec != '0':
        dec_words = DECIMAL_SEPARATOR + _natural_words(str_dec) + \
                    DECIMAL_PLACES[len(str_dec)]
        return negative + _natural_words(str_int) + dec_words

    return negative + _natural_words(str_int)


def _natural_words(str_int: str) -> str:
    length = len(str_int)
    if length > len(CLASSES) * 3:
        raise ValueError('out of range')

    modulo_3 = length % 3
    if modulo_3:
        str_int = '0' * (3 - modulo_3) + str_int
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    natural_words = ''
    while group > 0:
        three_digit = str_int[group * 3 - 3:group * 3]
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
