
def threedigit_words(threedigit):
    yekan = [u'',
             u'يک',
             u'دو',
             u'سه',
             u'چهار',
             u'پنج',
             u'شش',
             u'هفت',
             u'هشت',
             u'نه']
    
    dahgan = [u'',
              u'',
              u'بيست',
              u'سي',
              u'چهل',
              u'پنجاه',
              u'شصت',
              u'هفتاد',
              u'هشتاد',
              u'نود']
    
    sadgan = [u'',
              u'يکصد',
              u'دويست',
              u'سيصد',
              u'چهارصد',
              u'پانصد',
              u'ششصد',
              u'هفتصد',
              u'هشتصد',
              u'نهصد']

    exceptions = [u'ده',
                  u'يازده',
                  u'دوازده',
                  u'سيزده',
                  u'چهارده',
                  u'پانزده',
                  u'شانزده',
                  u'هفده',
                  u'هجده',
                  u'نوزده']

    words = ''
        
    words = sadgan[int(threedigit[0])] +\
            (u' و ' if threedigit[0] != '0' and threedigit[1:]!='00'  else '')
    if threedigit[1] == '1':
        words += exceptions[int(threedigit[2])]
    else:
        words += dahgan[int(threedigit[1])] +\
                 (u' و ' if threedigit[2] != '0' and threedigit[1]!='0' else '')
        words += yekan[int(threedigit[2])]
    return words

def strnum2words(strnumber):
    if int(strnumber) == 0:
        return 'صفر'

    scale = [u'',
            u' هزار',
            u' ميليون ',
            u' ميليارد',
            u' بيليون',
            u' بيليارد',
            u' تريليون',
            u' ترليارد',
            u' کوآدريليون',
            u' کادريليارد'
            u' کوينتيليون',
             u' کوانتينيارد']

    if len(strnumber) > len(scale) * 3:
        raise ValueError, 'Out of range!'
    
    length = len(strnumber)
    
    if length%3 !=0:
        strnumber = '0'*(3-length%3) + strnumber
        
    groups = len(strnumber)/3
    words = ''
    group = groups
    while group > 0:
        threedigit = strnumber[group*3-3:group*3]
        word3 = threedigit_words(threedigit)
        
        if word3 != '' and group != groups:
            if words == '':
                words = word3 + scale[groups-group]
            else:
                words = word3 + scale[groups-group] + u' و ' + words
        else:
            words = word3 + words

        group -= 1
    return words

                     
while True:
    number = raw_input('Enter your number plz:\n')
    print strnum2words(number)
