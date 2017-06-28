"""Provide functions to convert a number (int) to Persian words."""


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
    d1, d2, d3 = threedigit
    if d1 != '0' and threedigit[1:] != '00':
        words = SADGAN[int(d1)] + ' و '
    else:
        words = SADGAN[int(d1)]
    if d2 == '1':
        words += DAH_TA_BIST[int(d3)]
    else:
        if d3 != '0' and d2 != '0':
            words += DAHGAN[int(d2)] + ' و '
        else:
            words += DAHGAN[int(d2)]
        words += YEKAN[int(d3)]
    return words


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
