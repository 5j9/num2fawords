"""Provide functions to convert a number (int) to Persian words."""

from typing import Union

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


def _three_digit_words(threedigit: str):
    """Return the word representation of threedigit."""
    sadgan, dahgan, yekan = threedigit
    if sadgan == '0' or threedigit[1:] == '00':
        words = SADGAN[int(sadgan)]
    else:
        words = SADGAN[int(sadgan)] + ' و '
    if dahgan == '1':
        return DAH_TA_BIST[int(yekan)]
    if yekan == '0' or dahgan == '0':
        words += DAHGAN[int(dahgan)]
    else:
        words += DAHGAN[int(dahgan)] + ' و '
    return words + YEKAN[int(yekan)]


def cardinal_words(number: Union[str, int]):
    int_num = int(number)
    str_num = str(int_num)
    if int_num == 0:
        return 'صفر'
    if int_num < 0:
        str_num = str_num[1:]
        negative = 'منفی '
    else:
        negative = ''

    if len(str_num) > len(SCALE) * 3:
        raise ValueError('out of range')

    length = len(str_num)

    modulo_3 = length % 3
    if modulo_3:
        str_num = '0' * (3 - modulo_3) + str_num
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    words = ''
    while group > 0:
        three_digit = str_num[group * 3 - 3:group * 3]
        word3 = _three_digit_words(three_digit)
        if word3 and group != groups:
            if words:
                words = word3 + SCALE[groups - group] + ' و ' + words
            else:
                words = word3 + SCALE[groups - group]
        else:
            words = word3 + words
        group -= 1

    return negative + words


def ordinal_words(digits: Union[str, int]):
    """Return the ordinal_words form of the digits converted to words."""
    words = cardinal_words(digits)
    if words[-2:] == 'سه':
        return words[:-2] + 'سوم'
    return words + 'م'


if __name__ == '__main__':
    while True:
        n = input('Enter your number:\n')
        print(cardinal_words(n))
        print(ordinal_words(n))
