"""Provide a command-line interface to use cardinal_words and ordinal_words."""

from argparse import ArgumentParser

from num2fawords import words, ordinal_words


parser = ArgumentParser()
parser.add_argument(
    'number', help='the number that is going to be converted to words'
)
parser.add_argument(
    '--ordinal', '-o',
    help='convert to ordinal from', action='store_true',
)
args = parser.parse_args()
if args.ordinal:
    print(ordinal_words(args.number))
else:
    print(words(args.number))
