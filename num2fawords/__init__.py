"""Provide functions to convert a number (int) to Persian words."""

from typing import Union as _Union
from itertools import chain as _chain


YEKAN = [
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

DAHGAN = [
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

DAH_TA_BIST = [
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

SADGAN = [
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

SCALE = [
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

ASHAR = ['', ' دهم', ' صدم']
ASHAR.extend(_chain.from_iterable(
    (i, ' ده' + i, ' صد' + i)
    for i in (i + 'م' for i in SCALE[1:])
))

MOMAYEZ = ' ممیز '


def _three_digit_words(threedigit: str) -> str:
    """Return the word representation of threedigit."""
    sadgan, dahgan, yekan = threedigit
    if sadgan == '0' or threedigit[1:] == '00':
        words = SADGAN[int(sadgan)]
    else:
        words = SADGAN[int(sadgan)] + ' و '
    if dahgan == '1':
        return words + DAH_TA_BIST[int(yekan)]
    if yekan == '0' or dahgan == '0':
        words += DAHGAN[int(dahgan)]
    else:
        words += DAHGAN[int(dahgan)] + ' و '
    return words + YEKAN[int(yekan)]


def cardinal_words(number: _Union[int, float, str]) -> str:
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
            # Todo: Can the exponent be out of ASHAR range? Raise ValueError.
            if base[1:2] == '.':
                return cardinal_words(base[:1] + base[2:]) + \
                       ASHAR[int(exponent) + len(base) - 2]
            else:
                return cardinal_words(base) + \
                       ASHAR[int(exponent)]
        str_int, _, str_dec = str_num.rpartition('.')
        int_dec = int(str_dec)
        if str_int == '0':
            return cardinal_words(int_dec) + ASHAR[len(str_dec)]
        if int_dec:
            dec_words = MOMAYEZ + cardinal_words(int_dec) + \
                        ASHAR[len(str_dec)]
        else:
            dec_words = ''
    else:
        str_int = str_num
        dec_words = ''

    length = len(str_int)
    if length > len(SCALE) * 3:
        raise ValueError('out of range')

    modulo_3 = length % 3
    if modulo_3:
        str_int = '0' * (3 - modulo_3) + str_int
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    words = ''
    while group > 0:
        three_digit = str_int[group * 3 - 3:group * 3]
        word3 = _three_digit_words(three_digit)
        if word3 and group != groups:
            if words:
                words = word3 + SCALE[groups - group] + ' و ' + words
            else:
                words = word3 + SCALE[groups - group]
        else:
            words = word3 + words
        group -= 1

    return negative + words + dec_words


def ordinal_words(number: _Union[int, str])-> str:
    """Return the ordinal_words form of the number converted to words."""
    words = cardinal_words(number)
    if words[-2:] == 'سه':
        return words[:-2] + 'سوم'
    return words + 'م'
