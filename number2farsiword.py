"""Provide functions to convert a number (int) to Persian words."""

from itertools import islice


YEKAN = {
    '0': '',
    '1': 'یک',
    '2': 'دو',
    '3': 'سه',
    '4': 'چهار',
    '5': 'پنج',
    '6': 'شش',
    '7': 'هفت',
    '8': 'هشت',
    '9': 'نه',
}

DAHGAN = {
    '0': '',
    '2': 'بیست',
    '3': 'سی',
    '4': 'چهل',
    '5': 'پنجاه',
    '6': 'شصت',
    '7': 'هفتاد',
    '8': 'هشتاد',
    '9': 'نود',
}

DAH_TA_BIST = {
    '0': 'ده',
    '1': 'یازده',
    '2': 'دوازده',
    '3': 'سیزده',
    '4': 'چهارده',
    '5': 'پانزده',
    '6': 'شانزده',
    '7': 'هفده',
    '8': 'هجده',
    '9': 'نوزده',
}

SADGAN = {
    '0': '',
    '1': 'یکصد',
    '2': 'دویست',
    '3': 'سیصد',
    '4': 'چهارصد',
    '5': 'پانصد',
    '6': 'ششصد',
    '7': 'هفتصد',
    '8': 'هشتصد',
    '9': 'نهصد',
}

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


def _three_digit_words(threedigit):
    """Return the word representation of threedigit."""
    sadgan, dahgan, yekan = threedigit
    if sadgan == '0' or threedigit[1:] == '00':
        words = SADGAN[sadgan]
    else:
        words = SADGAN[sadgan] + ' و '
    if dahgan == '1':
        return DAH_TA_BIST[yekan]
    if yekan == '0' or dahgan == '0':
        words += DAHGAN[dahgan]
    else:
        words += DAHGAN[dahgan] + ' و '
    return words + YEKAN[yekan]


def cardinal(strnumber):
    if int(strnumber) == 0:
        return 'صفر'

    if len(strnumber) > len(SCALE) * 3:
        raise ValueError('out of range')

    length = len(strnumber)

    modulo_3 = length % 3
    if modulo_3:
        strnumber = '0' * (3 - modulo_3) + strnumber
        length += 3 - modulo_3

    groups = length // 3
    words = ''
    group = groups
    while group > 0:
        three_digit = strnumber[group * 3 - 3:group * 3]
        word3 = _three_digit_words(three_digit)
        if word3 and group != groups:
            if words == '':
                words = word3 + SCALE[groups - group]
            else:
                words = word3 + SCALE[groups - group] + ' و ' + words
        else:
            words = word3 + words
        group -= 1
    return words


def ordinal(number):
    """Return the ordinal form of the number converted to words."""
    words = cardinal(number)
    if words[-2:] == 'سه':
        return words[:-2] + 'سوم'
    return words + 'م'


if __name__ == '__main__':
    while True:
        n = input('Enter your number plz:\n')
        print(cardinal(n))
        print(ordinal(n))
