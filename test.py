from unittest import TestCase, main
from number2farsiword import int_to_cardinal, int_to_ordinal


class Number2FarsiWord(TestCase):

    """Test number2farsiword module."""

    def test_cardinal(self):
        """Test the int_to_cardinal function."""
        self.assertEqual(int_to_cardinal('0'), 'صفر')
        self.assertEqual(int_to_cardinal('1'), 'یک')
        self.assertEqual(int_to_cardinal('2'), 'دو')
        self.assertEqual(int_to_cardinal('3'), 'سه')
        self.assertEqual(int_to_cardinal('4'), 'چهار')
        self.assertEqual(int_to_cardinal('5'), 'پنج')
        self.assertEqual(int_to_cardinal('6'), 'شش')
        self.assertEqual(int_to_cardinal('7'), 'هفت')
        self.assertEqual(int_to_cardinal('8'), 'هشت')
        self.assertEqual(int_to_cardinal('9'), 'نه')
        self.assertEqual(int_to_cardinal('10'), 'ده')
        self.assertEqual(int_to_cardinal('11'), 'یازده')
        self.assertEqual(int_to_cardinal('12'), 'دوازده')
        self.assertEqual(int_to_cardinal('13'), 'سیزده')
        self.assertEqual(int_to_cardinal('14'), 'چهارده')
        self.assertEqual(int_to_cardinal('15'), 'پانزده')
        self.assertEqual(int_to_cardinal('16'), 'شانزده')
        self.assertEqual(int_to_cardinal('17'), 'هفده')
        self.assertEqual(int_to_cardinal('18'), 'هجده')
        self.assertEqual(int_to_cardinal('19'), 'نوزده')
        self.assertEqual(int_to_cardinal('20'), 'بیست')
        self.assertEqual(int_to_cardinal('21'), 'بیست و یک')
        self.assertEqual(int_to_cardinal('22'), 'بیست و دو')
        self.assertEqual(int_to_cardinal('23'), 'بیست و سه')
        self.assertEqual(int_to_cardinal('24'), 'بیست و چهار')
        self.assertEqual(int_to_cardinal('29'), 'بیست و نه')
        self.assertEqual(int_to_cardinal('30'), 'سی')
        self.assertEqual(int_to_cardinal('35'), 'سی و پنج')
        self.assertEqual(int_to_cardinal('44'), 'چهل و چهار')
        self.assertEqual(int_to_cardinal('57'), 'پنجاه و هفت')
        self.assertEqual(int_to_cardinal('61'), 'شصت و یک')
        self.assertEqual(int_to_cardinal('78'), 'هفتاد و هشت')
        self.assertEqual(int_to_cardinal('80'), 'هشتاد')
        self.assertEqual(int_to_cardinal('93'), 'نود و سه')
        self.assertEqual(int_to_cardinal('100'), 'یکصد')
        self.assertEqual(int_to_cardinal('101'), 'یکصد و یک')
        self.assertEqual(int_to_cardinal('1235'), 'یک هزار و دویست و سی و پنج')
        self.assertEqual(
            int_to_cardinal('99999999'),
            'نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه',
        )
        self.assertEqual(
            int_to_cardinal('999999999999999999'),
            'نهصد و نود و نه بیلیارد'
            ' و نهصد و نود و نه بیلیون'
            ' و نهصد و نود و نه میلیارد'
            ' و نهصد و نود و نه میلیون'
            ' و نهصد و نود و نه هزار'
            ' و نهصد و نود و نه',
        )

    def test_accepts_unicode_digits(self):
        self.assertEqual(int_to_cardinal('۰'), 'صفر')
        self.assertEqual(int_to_ordinal('۰'), 'صفرم')

    def test_negative_nubmers(self):
        self.assertEqual(int_to_cardinal('-5'), 'منفی پنج')
        self.assertEqual(int_to_cardinal(-5), 'منفی پنج')

    def test_ordinal(self):
        """Test the int_to_ordinal function."""
        self.assertEqual(int_to_ordinal('0'), 'صفرم')
        self.assertEqual(int_to_ordinal('1'), 'یکم')
        self.assertEqual(int_to_ordinal('2'), 'دوم')
        self.assertEqual(int_to_ordinal('3'), 'سوم')
        self.assertEqual(int_to_ordinal('4'), 'چهارم')
        self.assertEqual(int_to_ordinal('5'), 'پنجم')
        self.assertEqual(int_to_ordinal('6'), 'ششم')
        self.assertEqual(int_to_ordinal('7'), 'هفتم')
        self.assertEqual(int_to_ordinal('8'), 'هشتم')
        self.assertEqual(int_to_ordinal('9'), 'نهم')
        self.assertEqual(int_to_ordinal('10'), 'دهم')
        self.assertEqual(int_to_ordinal('11'), 'یازدهم')
        self.assertEqual(int_to_ordinal('12'), 'دوازدهم')
        self.assertEqual(int_to_ordinal('13'), 'سیزدهم')
        self.assertEqual(int_to_ordinal('14'), 'چهاردهم')
        self.assertEqual(int_to_ordinal('15'), 'پانزدهم')
        self.assertEqual(int_to_ordinal('16'), 'شانزدهم')
        self.assertEqual(int_to_ordinal('17'), 'هفدهم')
        self.assertEqual(int_to_ordinal('18'), 'هجدهم')
        self.assertEqual(int_to_ordinal('19'), 'نوزدهم')
        self.assertEqual(int_to_ordinal('20'), 'بیستم')
        self.assertEqual(int_to_ordinal('21'), 'بیست و یکم')
        self.assertEqual(int_to_ordinal('22'), 'بیست و دوم')
        self.assertEqual(int_to_ordinal('23'), 'بیست و سوم')
        self.assertEqual(int_to_ordinal('24'), 'بیست و چهارم')
        self.assertEqual(int_to_ordinal('1999'), 'یک هزار و نهصد و نود و نهم')
        self.assertEqual(int_to_ordinal('10666'), 'ده هزار و ششصد و شصت و ششم')
        self.assertEqual(int_to_ordinal(
            '999555'), 'نهصد و نود و نه هزار و پانصد و پنجاه و پنجم'
        )
        # self.assertEqual(int_to_ordinal('1000000'), 'یک میلیونم')


if __name__ == '__main':
    main()
