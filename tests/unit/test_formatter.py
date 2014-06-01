from minibar.formatter import Formatter
from unittest import TestCase
import pyshould.patch


class TestFormatter(TestCase):
    def setUp(self):
        self.formatter = Formatter()

    def test_get_value_args(self):
        self.formatter.get_value(0,
                                 [1], {2: 'b'}).should.integer.eq(1)

    def test_get_value_kwargs(self):
        self.formatter.get_value(
            u'string_a',
            [1], {'string_a': 'string_b'}).should.eq('string_b')

    def test_get_value_colors(self):
        self.formatter.get_value(
            u'black',
            [1], {'string_a':'string_b'}).should.eq('\033[30m')

    def test_get_value_else(self):
        self.formatter.get_value(
            u'string_a',
            [1], {'string_c':'string_b'}).should.eq('{string_a}')
