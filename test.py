from unittest import TestCase, main
from number2farsiword import cardinal_words, ordinal_words


class Number2FarsiWord(TestCase):

    """Test number2farsiword module."""

    def test_cardinal(self):
        """Test the cardinal_words function."""
        self.assertEqual(cardinal_words('0'), 'صفر')
        self.assertEqual(cardinal_words('1'), 'یک')
        self.assertEqual(cardinal_words('2'), 'دو')
        self.assertEqual(cardinal_words('3'), 'سه')
        self.assertEqual(cardinal_words('4'), 'چهار')
        self.assertEqual(cardinal_words('5'), 'پنج')
        self.assertEqual(cardinal_words('6'), 'شش')
        self.assertEqual(cardinal_words('7'), 'هفت')
        self.assertEqual(cardinal_words('8'), 'هشت')
        self.assertEqual(cardinal_words('9'), 'نه')
        self.assertEqual(cardinal_words('10'), 'ده')
        self.assertEqual(cardinal_words('11'), 'یازده')
        self.assertEqual(cardinal_words('12'), 'دوازده')
        self.assertEqual(cardinal_words('13'), 'سیزده')
        self.assertEqual(cardinal_words('14'), 'چهارده')
        self.assertEqual(cardinal_words('15'), 'پانزده')
        self.assertEqual(cardinal_words('16'), 'شانزده')
        self.assertEqual(cardinal_words('17'), 'هفده')
        self.assertEqual(cardinal_words('18'), 'هجده')
        self.assertEqual(cardinal_words('19'), 'نوزده')
        self.assertEqual(cardinal_words('20'), 'بیست')
        self.assertEqual(cardinal_words('21'), 'بیست و یک')
        self.assertEqual(cardinal_words('22'), 'بیست و دو')
        self.assertEqual(cardinal_words('23'), 'بیست و سه')
        self.assertEqual(cardinal_words('24'), 'بیست و چهار')
        self.assertEqual(cardinal_words('29'), 'بیست و نه')
        self.assertEqual(cardinal_words('30'), 'سی')
        self.assertEqual(cardinal_words('35'), 'سی و پنج')
        self.assertEqual(cardinal_words('44'), 'چهل و چهار')
        self.assertEqual(cardinal_words('57'), 'پنجاه و هفت')
        self.assertEqual(cardinal_words('61'), 'شصت و یک')
        self.assertEqual(cardinal_words('78'), 'هفتاد و هشت')
        self.assertEqual(cardinal_words('80'), 'هشتاد')
        self.assertEqual(cardinal_words('93'), 'نود و سه')
        self.assertEqual(cardinal_words('100'), 'یکصد')
        self.assertEqual(cardinal_words('101'), 'یکصد و یک')
        self.assertEqual(cardinal_words('1235'), 'یک هزار و دویست و سی و پنج')
        self.assertEqual(
            cardinal_words('99999999'),
            'نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه',
        )
        self.assertEqual(
            cardinal_words('999999999999999999'),
            'نهصد و نود و نه بیلیارد'
            ' و نهصد و نود و نه بیلیون'
            ' و نهصد و نود و نه میلیارد'
            ' و نهصد و نود و نه میلیون'
            ' و نهصد و نود و نه هزار'
            ' و نهصد و نود و نه',
        )

    def test_accepts_unicode_digits(self):
        self.assertEqual(cardinal_words('۰'), 'صفر')
        self.assertEqual(ordinal_words('۰'), 'صفرم')

    def test_negative_nubmers(self):
        self.assertEqual(cardinal_words('-5'), 'منفی پنج')
        self.assertEqual(cardinal_words(-5), 'منفی پنج')

    def test_ordinal(self):
        """Test the ordinal_words function."""
        self.assertEqual(ordinal_words('0'), 'صفرم')
        self.assertEqual(ordinal_words('1'), 'یکم')
        self.assertEqual(ordinal_words('2'), 'دوم')
        self.assertEqual(ordinal_words('3'), 'سوم')
        self.assertEqual(ordinal_words('4'), 'چهارم')
        self.assertEqual(ordinal_words('5'), 'پنجم')
        self.assertEqual(ordinal_words('6'), 'ششم')
        self.assertEqual(ordinal_words('7'), 'هفتم')
        self.assertEqual(ordinal_words('8'), 'هشتم')
        self.assertEqual(ordinal_words('9'), 'نهم')
        self.assertEqual(ordinal_words('10'), 'دهم')
        self.assertEqual(ordinal_words('11'), 'یازدهم')
        self.assertEqual(ordinal_words('12'), 'دوازدهم')
        self.assertEqual(ordinal_words('13'), 'سیزدهم')
        self.assertEqual(ordinal_words('14'), 'چهاردهم')
        self.assertEqual(ordinal_words('15'), 'پانزدهم')
        self.assertEqual(ordinal_words('16'), 'شانزدهم')
        self.assertEqual(ordinal_words('17'), 'هفدهم')
        self.assertEqual(ordinal_words('18'), 'هجدهم')
        self.assertEqual(ordinal_words('19'), 'نوزدهم')
        self.assertEqual(ordinal_words('20'), 'بیستم')
        self.assertEqual(ordinal_words('21'), 'بیست و یکم')
        self.assertEqual(ordinal_words('22'), 'بیست و دوم')
        self.assertEqual(ordinal_words('23'), 'بیست و سوم')
        self.assertEqual(ordinal_words('24'), 'بیست و چهارم')
        self.assertEqual(ordinal_words('1999'), 'یک هزار و نهصد و نود و نهم')
        self.assertEqual(ordinal_words('10666'), 'ده هزار و ششصد و شصت و ششم')
        self.assertEqual(ordinal_words(
            '999555'), 'نهصد و نود و نه هزار و پانصد و پنجاه و پنجم'
        )
        # self.assertEqual(ordinal_words('1000000'), 'یک میلیونم')


if __name__ == '__main':
    main()
