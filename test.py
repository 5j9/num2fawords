from unittest import TestCase, main
from number2farsiword import cardinal, ordinal


class Number2FarsiWord(TestCase):

    """Test number2farsiword module."""

    def test_cardinal(self):
        """Test the cardinal function."""
        self.assertEqual(cardinal('0'), 'صفر')
        self.assertEqual(cardinal('1'), 'یک')
        self.assertEqual(cardinal('2'), 'دو')
        self.assertEqual(cardinal('3'), 'سه')
        self.assertEqual(cardinal('4'), 'چهار')
        self.assertEqual(cardinal('5'), 'پنج')
        self.assertEqual(cardinal('6'), 'شش')
        self.assertEqual(cardinal('7'), 'هفت')
        self.assertEqual(cardinal('8'), 'هشت')
        self.assertEqual(cardinal('9'), 'نه')
        self.assertEqual(cardinal('10'), 'ده')
        self.assertEqual(cardinal('11'), 'یازده')
        self.assertEqual(cardinal('12'), 'دوازده')
        self.assertEqual(cardinal('13'), 'سیزده')
        self.assertEqual(cardinal('14'), 'چهارده')
        self.assertEqual(cardinal('15'), 'پانزده')
        self.assertEqual(cardinal('16'), 'شانزده')
        self.assertEqual(cardinal('17'), 'هفده')
        self.assertEqual(cardinal('18'), 'هجده')
        self.assertEqual(cardinal('19'), 'نوزده')
        self.assertEqual(cardinal('20'), 'بیست')
        self.assertEqual(cardinal('21'), 'بیست و یک')
        self.assertEqual(cardinal('22'), 'بیست و دو')
        self.assertEqual(cardinal('23'), 'بیست و سه')
        self.assertEqual(cardinal('24'), 'بیست و چهار')
        self.assertEqual(cardinal('29'), 'بیست و نه')
        self.assertEqual(cardinal('30'), 'سی')
        self.assertEqual(cardinal('35'), 'سی و پنج')
        self.assertEqual(cardinal('44'), 'چهل و چهار')
        self.assertEqual(cardinal('57'), 'پنجاه و هفت')
        self.assertEqual(cardinal('61'), 'شصت و یک')
        self.assertEqual(cardinal('78'), 'هفتاد و هشت')
        self.assertEqual(cardinal('80'), 'هشتاد')
        self.assertEqual(cardinal('93'), 'نود و سه')
        self.assertEqual(cardinal('100'), 'یکصد')
        self.assertEqual(cardinal('101'), 'یکصد و یک')
        self.assertEqual(cardinal('1235'), 'یک هزار و دویست و سی و پنج')
        self.assertEqual(
            cardinal('99999999'),
            'نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه',
        )
        self.assertEqual(
            cardinal('999999999999999999'),
            'نهصد و نود و نه بیلیارد'
            ' و نهصد و نود و نه بیلیون'
            ' و نهصد و نود و نه میلیارد'
            ' و نهصد و نود و نه میلیون'
            ' و نهصد و نود و نه هزار'
            ' و نهصد و نود و نه',
        )

    def test_accepts_unicode_digits(self):
        self.assertEqual(cardinal('۰'), 'صفر')
        self.assertEqual(ordinal('۰'), 'صفرم')

    def test_ordinal(self):
        """Test the ordinal function."""
        self.assertEqual(ordinal('0'), 'صفرم')
        self.assertEqual(ordinal('1'), 'یکم')
        self.assertEqual(ordinal('2'), 'دوم')
        self.assertEqual(ordinal('3'), 'سوم')
        self.assertEqual(ordinal('4'), 'چهارم')
        self.assertEqual(ordinal('5'), 'پنجم')
        self.assertEqual(ordinal('6'), 'ششم')
        self.assertEqual(ordinal('7'), 'هفتم')
        self.assertEqual(ordinal('8'), 'هشتم')
        self.assertEqual(ordinal('9'), 'نهم')
        self.assertEqual(ordinal('10'), 'دهم')
        self.assertEqual(ordinal('11'), 'یازدهم')
        self.assertEqual(ordinal('12'), 'دوازدهم')
        self.assertEqual(ordinal('13'), 'سیزدهم')
        self.assertEqual(ordinal('14'), 'چهاردهم')
        self.assertEqual(ordinal('15'), 'پانزدهم')
        self.assertEqual(ordinal('16'), 'شانزدهم')
        self.assertEqual(ordinal('17'), 'هفدهم')
        self.assertEqual(ordinal('18'), 'هجدهم')
        self.assertEqual(ordinal('19'), 'نوزدهم')
        self.assertEqual(ordinal('20'), 'بیستم')
        self.assertEqual(ordinal('21'), 'بیست و یکم')
        self.assertEqual(ordinal('22'), 'بیست و دوم')
        self.assertEqual(ordinal('23'), 'بیست و سوم')
        self.assertEqual(ordinal('24'), 'بیست و چهارم')
        self.assertEqual(ordinal('1999'), 'یک هزار و نهصد و نود و نهم')
        self.assertEqual(ordinal('10666'), 'ده هزار و ششصد و شصت و ششم')
        self.assertEqual(ordinal(
            '999555'), 'نهصد و نود و نه هزار و پانصد و پنجاه و پنجم'
        )
        # self.assertEqual(ordinal('1000000'), 'یک میلیونم')


if __name__ == '__main':
    main()
