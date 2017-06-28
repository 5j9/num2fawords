"""Provide functions to convert a number (int) to Persian words."""
#a Lua rewrite of this code is available at: http://fa.wikipedia.org/wiki/پودمان:عدد_به_حروف

YEKAN = [
    '',
    'يک',
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
    'بيست',
    'سي',
    'چهل',
    'پنجاه',
    'شصت',
    'هفتاد',
    'هشتاد',
    'نود',
]

SADGAN = [
    '',
    'يکصد',
    'دويست',
    'سيصد',
    'چهارصد',
    'پانصد',
    'ششصد',
    'هفتصد',
    'هشتصد',
    'نهصد',
]

DAH_TA_BIST = [
    'ده',
    'يازده',
    'دوازده',
    'سيزده',
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
    ' ميليون ',
    ' ميليارد',
    ' بيليون',
    ' بيليارد',
    ' تريليون',
    ' ترليارد',
    ' کوآدريليون',
    ' کادريليارد',
    ' کوينتيليون',
    ' کوانتينيارد',
]


def _three_digit_words(threedigit):
    if threedigit[0] != '0' and threedigit[1:] != '00':
        words = SADGAN[int(threedigit[0])] + ' و '
    else:
        words = SADGAN[int(threedigit[0])]
    if threedigit[1] == '1':
        words += DAH_TA_BIST[int(threedigit[2])]
    else:
        if threedigit[2] != '0' and threedigit[1] != '0':
            words += DAHGAN[int(threedigit[1])] + ' و '
        else:
            words += DAHGAN[int(threedigit[1])]
        words += YEKAN[int(threedigit[2])]
    return words


def cardinal(strnumber):
    if int(strnumber) == 0:
        return 'صفر'

    if len(strnumber) > len(SCALE) * 3:
        raise ValueError('out of range')

    length = len(strnumber)

    if length % 3 != 0:
        strnumber = '0' * (3-length % 3) + strnumber

    groups = len(strnumber) // 3
    words = ''
    group = groups
    while group > 0:
        threedigit = strnumber[group * 3 - 3:group * 3]
        word3 = _three_digit_words(threedigit)
        
        if word3 != '' and group != groups:
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
