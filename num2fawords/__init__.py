"""Provide functions to convert a number (int) to Persian words."""

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


def words(number: _Union[int, float, str]) -> str:
    if isinstance(number, str):
        str_num = number
        try:
            number = int(number)
        except ValueError:
            number = float(number)
    else:
        str_num = str(number)

    if number == 0:
        return 'صفر'
    if number < 0:
        str_num = str_num[1:]
        negative = 'منفی '
    else:
        negative = ''

    if isinstance(number, float):
        base, e_, exponent = str_num.rpartition('e-')
        if e_:
            # Todo: Can the exponent be out of DECIMAL_PLACES range? If yes,
            # raise ValueError.
            if base[1:2] == '.':
                return words(base[:1] + base[2:]) + \
                       DECIMAL_PLACES[int(exponent) + len(base) - 2]
            else:
                return words(base) + \
                       DECIMAL_PLACES[int(exponent)]
        str_int, _, str_dec = str_num.rpartition('.')
        int_dec = int(str_dec)
        if str_int == '0':
            return words(int_dec) + DECIMAL_PLACES[len(str_dec)]
        if int_dec:
            dec_words = DECIMAL_SEPARATOR + words(int_dec) + \
                        DECIMAL_PLACES[len(str_dec)]
        else:
            dec_words = ''
    else:
        str_int = str_num
        dec_words = ''

    length = len(str_int)
    if length > len(CLASSES) * 3:
        raise ValueError('out of range')

    modulo_3 = length % 3
    if modulo_3:
        str_int = '0' * (3 - modulo_3) + str_int
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    int_words = ''
    while group > 0:
        three_digit = str_int[group * 3 - 3:group * 3]
        word3 = _three_digit_words(three_digit)
        if word3 and group != groups:
            if int_words:
                int_words = word3 + CLASSES[groups - group] + ' و ' + int_words
            else:
                int_words = word3 + CLASSES[groups - group]
        else:
            int_words = word3 + int_words
        group -= 1

    return negative + int_words + dec_words


def ordinal_words(number: _Union[int, str])-> str:
    """Return the ordinal_words form of the number converted to words."""
    w = words(number)
    if w[-2:] == 'سه':
        return w[:-2] + 'سوم'
    return w + 'م'
