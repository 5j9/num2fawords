from fractions import Fraction
from decimal import Decimal
from math import pi
from unittest import TestCase, main

from num2fawords import words, ordinal_words, change_defaults


class Number2FarsiWord(TestCase):

    """Test number2farsiword module."""

    def test_non_negative(self):
        """Test the words function."""
        assert_equal = self.assertEqual
        assert_equal(words(0), 'صفر')
        assert_equal(words('0'), 'صفر')
        assert_equal(words(1), 'یک')
        assert_equal(words(2), 'دو')
        assert_equal(words(3), 'سه')
        assert_equal(words(4), 'چهار')
        assert_equal(words(5), 'پنج')
        assert_equal(words(6), 'شش')
        assert_equal(words(7), 'هفت')
        assert_equal(words(8), 'هشت')
        assert_equal(words(9), 'نه')
        assert_equal(words(10), 'ده')
        assert_equal(words(11), 'یازده')
        assert_equal(words(12), 'دوازده')
        assert_equal(words(13), 'سیزده')
        assert_equal(words(14), 'چهارده')
        assert_equal(words(15), 'پانزده')
        assert_equal(words(16), 'شانزده')
        assert_equal(words(17), 'هفده')
        assert_equal(words(18), 'هجده')
        assert_equal(words(19), 'نوزده')
        assert_equal(words(20), 'بیست')
        assert_equal(words(21), 'بیست و یک')
        assert_equal(words(22), 'بیست و دو')
        assert_equal(words(23), 'بیست و سه')
        assert_equal(words(24), 'بیست و چهار')
        assert_equal(words(29), 'بیست و نه')
        assert_equal(words(30), 'سی')
        assert_equal(words(35), 'سی و پنج')
        assert_equal(words(44), 'چهل و چهار')
        assert_equal(words(57), 'پنجاه و هفت')
        assert_equal(words(61), 'شصت و یک')
        assert_equal(words(78), 'هفتاد و هشت')
        assert_equal(words(80), 'هشتاد')
        assert_equal(words(93), 'نود و سه')
        assert_equal(words(100), 'یکصد')
        assert_equal(words(101), 'یکصد و یک')
        assert_equal(words(1235), 'یک هزار و دویست و سی و پنج')
        assert_equal(
            words(99999999),
            'نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه',
        )
        assert_equal(
            words(999999999999999999),
            'نهصد و نود و نه بیلیارد'
            ' و نهصد و نود و نه بیلیون'
            ' و نهصد و نود و نه میلیارد'
            ' و نهصد و نود و نه میلیون'
            ' و نهصد و نود و نه هزار'
            ' و نهصد و نود و نه',
        )

    def test_negative_numbers(self):
        assert_equal = self.assertEqual
        assert_equal(ordinal_words(-5), 'منفی پنجم')
        assert_equal(words(-5), 'منفی پنج')
        assert_equal(words('-5.5'), 'منفی پنج و پنج دهم')

    def test_non_negative_ordinal_words(self):
        """Test the ordinal_words function."""
        assert_equal = self.assertEqual
        assert_equal(ordinal_words(0), 'صفرم')
        assert_equal(ordinal_words('0'), 'صفرم')
        assert_equal(ordinal_words(1), 'یکم')
        assert_equal(ordinal_words(2), 'دوم')
        assert_equal(ordinal_words(3), 'سوم')
        assert_equal(ordinal_words(4), 'چهارم')
        assert_equal(ordinal_words(5), 'پنجم')
        assert_equal(ordinal_words(6), 'ششم')
        assert_equal(ordinal_words(7), 'هفتم')
        assert_equal(ordinal_words(8), 'هشتم')
        assert_equal(ordinal_words(9), 'نهم')
        assert_equal(ordinal_words(10), 'دهم')
        assert_equal(ordinal_words(11), 'یازدهم')
        assert_equal(ordinal_words(12), 'دوازدهم')
        assert_equal(ordinal_words(13), 'سیزدهم')
        assert_equal(ordinal_words(14), 'چهاردهم')
        assert_equal(ordinal_words(15), 'پانزدهم')
        assert_equal(ordinal_words(16), 'شانزدهم')
        assert_equal(ordinal_words(17), 'هفدهم')
        assert_equal(ordinal_words(18), 'هجدهم')
        assert_equal(ordinal_words(19), 'نوزدهم')
        assert_equal(ordinal_words(20), 'بیستم')
        assert_equal(ordinal_words(21), 'بیست و یکم')
        assert_equal(ordinal_words(22), 'بیست و دوم')
        assert_equal(ordinal_words(23), 'بیست و سوم')
        assert_equal(ordinal_words(24), 'بیست و چهارم')
        assert_equal(ordinal_words(111), 'یکصد و یازدهم')
        assert_equal(ordinal_words(1999), 'یک هزار و نهصد و نود و نهم')
        assert_equal(ordinal_words(10666), 'ده هزار و ششصد و شصت و ششم')
        assert_equal(
            ordinal_words(999555),
            'نهصد و نود و نه هزار و پانصد و پنجاه و پنجم',
        )
        assert_equal(ordinal_words(1000000), 'یک میلیونم')

    def test_float(self):
        assert_equal = self.assertEqual
        assert_equal(words(0.0), 'صفر')
        assert_equal(words('0.0'), 'صفر')
        assert_equal(words(1.0), 'یک')
        assert_equal(words(1.1), 'یک و یک دهم')
        assert_equal(words(1.100), 'یک و یک دهم')
        assert_equal(words(0.001), 'یک هزارم')
        assert_equal(words(0.1001), 'یک هزار و یک ده هزارم')
        assert_equal(words(5.45), 'پنج و چهل و پنج صدم')
        assert_equal(words(1e-3), 'یک هزارم')
        assert_equal(words(1E-3), 'یک هزارم')
        assert_equal(words('1e-3'), 'یک در ده به توان منفی سه')
        assert_equal(words('1E-3'), 'یک در ده به توان منفی سه')
        assert_equal(words(1e-6), 'یک در ده به توان منفی شش')
        assert_equal(words(1E-6), 'یک در ده به توان منفی شش')

        assert_equal(words(0.000001), 'یک در ده به توان منفی شش')
        assert_equal(words('0.000001'), 'یک میلیونم')

        assert_equal(
            words(0.0000011),
            'یک و یک دهم در ده به توان منفی شش'
        )
        assert_equal(words('0.0000011'), 'یازده ده میلیونم',)

        assert_equal(
            words(0.00000111),
            'یک و یازده صدم در ده به توان منفی شش',
        )
        assert_equal(words('0.00000111'), 'یکصد و یازده صد میلیونم')

        assert_equal(
            words(0.000001111),
            'یک و یکصد و یازده هزارم در ده به توان منفی شش',
        )
        assert_equal(
            words('0.000001111'), 'یک هزار و یکصد و یازده میلیاردم'
        )

    def test_value_errors(self):
        self.assertRaises(
            ValueError,
            words,
            1234567890123456789012345678901234567
        )

    def test_str_input(self):
        assert_equal = self.assertEqual
        assert_equal(words('42'), 'چهل و دو')
        assert_equal(words('\t\n 42 \n\t'), 'چهل و دو')
        assert_equal(words('3.14'), 'سه و چهارده صدم')
        assert_equal(words('+1.1', positive='مثبت '), 'مثبت یک و یک دهم')
        assert_equal(words('1e2'), 'یک در ده به توان دو')
        assert_equal(words('1E2'), 'یک در ده به توان دو')

    def test_decimal_input(self):
        self.assertEqual(words(Decimal('3.0')), 'سه')
        self.assertEqual(words(Decimal('-3.14')), 'منفی سه و چهارده صدم')
        # Let's go beyond floats
        beyond_float = words(Decimal(str(pi) + '238'))
        self.assertNotEqual(beyond_float, words(pi))
        self.assertTrue(beyond_float.endswith(''))
        # Decimal(float('1.1'))
        # == Decimal('1.100000000000000088817841970012523233890533447265625')
        self.assertRaises(ValueError, words, Decimal(1.1))

    def test_unsupported_input_type(self):
        self.assertRaises(TypeError, words, [])

    def test_fractions(self):
        assert_equal = self.assertEqual
        assert_equal(words(Fraction(16, -10)), 'منفی هشت پنجم')
        assert_equal(words(Fraction(Decimal('1.1'))), 'یازده دهم')
        assert_equal(words('-8/4'), 'منفی هشت چهارم')
        assert_equal(words(Fraction(0, 1)), 'صفر یکم')
        assert_equal(words('0/1'), 'صفر یکم')

    def test_persian_numbers(self):
        assert_equal = self.assertEqual
        assert_equal(words('۱'), 'یک')
        assert_equal(words('۱٫۱'), 'یک و یک دهم')
        assert_equal(words('۱٬۰۰۰'), 'یک هزار')

    def test_negative_float(self):
        assert_equal = self.assertEqual
        assert_equal(words(-1.1), 'منفی یک و یک دهم')

    def test_positive(self):
        assert_equal = self.assertEqual
        assert_equal(words(0, positive='مثبت '), 'صفر')
        assert_equal(words(7, positive='مثبت '), 'مثبت هفت')
        assert_equal(
            words(Fraction('1/2'), positive='مثبت '),
            'مثبت یک دوم',
        )
        assert_equal(
            words('1.1e+9', positive='مثبت '),
            'مثبت یک و یک دهم در ده به توان مثبت نه',
        )
        assert_equal(
            words(1.1e+9, positive='مثبت '),  # str(-1.1e+9) == 1100000000.0
            'مثبت یک میلیارد و یکصد میلیون',
        )

    def test_negative(self):
        assert_equal = self.assertEqual
        assert_equal(words(-2, negative='منهای '), 'منهای دو')
        assert_equal(words('-2', negative='منهای '), 'منهای دو')
        assert_equal(words(-1.1, negative='منهای '), 'منهای یک و یک دهم')
        assert_equal(words('-1.1', negative='منهای '), 'منهای یک و یک دهم')
        assert_equal(
            words(-1.1e-06, negative='منهای '),
            'منهای یک و یک دهم در ده به توان منهای شش',
        )
        assert_equal(
            words('-1/2', negative='منهای '),
            'منهای یک دوم',
        )
        assert_equal(
            words(Fraction(1, -2), negative='منهای '),
            'منهای یک دوم',
        )

    def test_fraction_separator(self):
        assert_equal = self.assertEqual
        assert_equal(
            words(
                '1/2',
                fraction_separator=' تقسیم بر ',
                ordinal_denominator=False,
            ),
            'یک تقسیم بر دو',
        )
        assert_equal(
            words(
                Fraction(4, -8),
                negative='منهای ',
                fraction_separator=' تقسیم بر ',
                ordinal_denominator=False,
            ),
            'منهای یک تقسیم بر دو',
        )

    def test_scientific_separator(self):
        assert_equal = self.assertEqual
        assert_equal(
            words(1.1e-9, scientific_separator=' ضربدر ده به قوهٔ '),
            'یک و یک دهم ضربدر ده به قوهٔ منفی نه',
        )
        assert_equal(
            words('1.1e-9', scientific_separator=' ضربدر ده به قوهٔ '),
            'یک و یک دهم ضربدر ده به قوهٔ منفی نه',
        )

    def test_scientific_fraction_separator(self):
        assert_equal = self.assertEqual
        assert_equal(
            words(
                '1/2',
                fraction_separator=' تقسیم بر ',
                ordinal_denominator=False
            ),
            'یک تقسیم بر دو',
        )
        assert_equal(
            words(
                Fraction(1, 2),
                fraction_separator=' تقسیم بر ',
                ordinal_denominator=False,
            ),
            'یک تقسیم بر دو',
        )

    def test_change_defaults(self):
        assert_equal = self.assertEqual
        change_defaults('مثبت ', 'منهای ')
        assert_equal(words('-۹'), 'منهای نه')
        assert_equal(words('+۹'), 'مثبت نه')
        change_defaults(decimal_separator=' ممیز ')
        assert_equal(words(1.1), 'مثبت یک ممیز یک دهم')
        change_defaults(fraction_separator=' روی ', ordinal_denominator=False)
        assert_equal(words('-1/10'), 'منهای یک روی ده')
        change_defaults(scientific_separator=' در ده به نمای ')
        assert_equal(words('1e2'), 'مثبت یک در ده به نمای مثبت دو')
        # Back to default
        change_defaults('', 'منفی ', ' و ', ' ', True, ' در ده به توان ')
        assert_equal(words(1.1), 'یک و یک دهم')
        assert_equal(words('1/2'), 'یک دوم')
        assert_equal(words('1e2'), 'یک در ده به توان دو')


if __name__ == '__main__':  # pragma: no cover
    main()
