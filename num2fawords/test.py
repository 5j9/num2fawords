from unittest import TestCase, main

from num2fawords import cardinal_words, ordinal_words


class Number2FarsiWord(TestCase):

    """Test number2farsiword module."""

    def test_non_negative_cardinal(self):
        """Test the cardinal_words function."""
        assert_equal = self.assertEqual
        assert_equal(cardinal_words(0), 'صفر')
        assert_equal(cardinal_words(1), 'یک')
        assert_equal(cardinal_words(2), 'دو')
        assert_equal(cardinal_words(3), 'سه')
        assert_equal(cardinal_words(4), 'چهار')
        assert_equal(cardinal_words(5), 'پنج')
        assert_equal(cardinal_words(6), 'شش')
        assert_equal(cardinal_words(7), 'هفت')
        assert_equal(cardinal_words(8), 'هشت')
        assert_equal(cardinal_words(9), 'نه')
        assert_equal(cardinal_words(10), 'ده')
        assert_equal(cardinal_words(11), 'یازده')
        assert_equal(cardinal_words(12), 'دوازده')
        assert_equal(cardinal_words(13), 'سیزده')
        assert_equal(cardinal_words(14), 'چهارده')
        assert_equal(cardinal_words(15), 'پانزده')
        assert_equal(cardinal_words(16), 'شانزده')
        assert_equal(cardinal_words(17), 'هفده')
        assert_equal(cardinal_words(18), 'هجده')
        assert_equal(cardinal_words(19), 'نوزده')
        assert_equal(cardinal_words(20), 'بیست')
        assert_equal(cardinal_words(21), 'بیست و یک')
        assert_equal(cardinal_words(22), 'بیست و دو')
        assert_equal(cardinal_words(23), 'بیست و سه')
        assert_equal(cardinal_words(24), 'بیست و چهار')
        assert_equal(cardinal_words(29), 'بیست و نه')
        assert_equal(cardinal_words(30), 'سی')
        assert_equal(cardinal_words(35), 'سی و پنج')
        assert_equal(cardinal_words(44), 'چهل و چهار')
        assert_equal(cardinal_words(57), 'پنجاه و هفت')
        assert_equal(cardinal_words(61), 'شصت و یک')
        assert_equal(cardinal_words(78), 'هفتاد و هشت')
        assert_equal(cardinal_words(80), 'هشتاد')
        assert_equal(cardinal_words(93), 'نود و سه')
        assert_equal(cardinal_words(100), 'یکصد')
        assert_equal(cardinal_words(101), 'یکصد و یک')
        assert_equal(cardinal_words(1235), 'یک هزار و دویست و سی و پنج')
        assert_equal(
            cardinal_words(99999999),
            'نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه',
        )
        assert_equal(
            cardinal_words(999999999999999999),
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
        assert_equal(cardinal_words(-5), 'منفی پنج')

    def test_non_negative_ordinal_words(self):
        """Test the ordinal_words function."""
        assert_equal = self.assertEqual
        assert_equal(ordinal_words(0), 'صفرم')
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
        assert_equal(cardinal_words(0.0), 'صفر')
        assert_equal(cardinal_words(1.0), 'یک')
        assert_equal(cardinal_words(1.1), 'یک و یک دهم')
        assert_equal(cardinal_words(1.100), 'یک و یک دهم')
        assert_equal(cardinal_words(0.001), 'یک هزارم')
        assert_equal(cardinal_words(0.1001), 'یک هزار و یک ده هزارم')
        assert_equal(cardinal_words(5.45), 'پنج و چهل و پنج صدم')
        assert_equal(cardinal_words(0.000001), 'یک میلیونم')
        assert_equal(cardinal_words(0.0000011), 'یازده ده میلیونم')
        assert_equal(cardinal_words(0.00000111), 'یکصد و یازده صد میلیونم')
        assert_equal(
            cardinal_words(0.000001111), 'یک هزار و یکصد و یازده میلیاردم'
        )

    def test_value_errors(self):
        self.assertRaises(
            ValueError,
            cardinal_words,
            1234567890123456789012345678901234567
        )

    def test_str_input(self):
        self.assertEqual(cardinal_words('42'), 'چهل و دو')
        self.assertEqual(cardinal_words('3.14'), 'سه و چهارده صدم')


if __name__ == '__main__':
    main()
