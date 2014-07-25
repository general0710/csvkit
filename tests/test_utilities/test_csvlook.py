#!/usr/bin/env python

import six

if six.PY3:
    from io import StringIO
else:
    from cStringIO import StringIO

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from csvkit.utilities.csvlook import CSVLook

class TestCSVLook(unittest.TestCase):
    def test_simple(self):
        args = ['examples/dummy3.csv']
        output_file = StringIO()
        utility = CSVLook(args, output_file)

        utility.main()

        input_file = StringIO(output_file.getvalue())

        self.assertEqual(next(input_file), '|----+---+----|\n')
        self.assertEqual(next(input_file), '|  a | b | c  |\n')
        self.assertEqual(next(input_file), '|----+---+----|\n')
        self.assertEqual(next(input_file), '|  1 | 2 | 3  |\n')
        self.assertEqual(next(input_file), '|  1 | 4 | 5  |\n')
        self.assertEqual(next(input_file), '|----+---+----|\n')

    def test_no_header(self):
        args = ['--no-header-row', 'examples/no_header_row3.csv']
        output_file = StringIO()
        utility = CSVLook(args, output_file)

        utility.main()

        input_file = StringIO(output_file.getvalue())

        #self.assertEqual(next(input_file), '|----+---+----|\n')
        #self.assertEqual(next(input_file), '|  1 | 2 | 3  |\n')
        #self.assertEqual(next(input_file), '|  4 | 5 | 6  |\n')
        #self.assertEqual(next(input_file), '|----+---+----|\n')

        self.assertEqual(next(input_file), '|----------+---------+----------|\n')
        self.assertEqual(next(input_file), '|  column1 | column2 | column3  |\n')
        self.assertEqual(next(input_file), '|----------+---------+----------|\n')
        self.assertEqual(next(input_file), '|  1       | 2       | 3        |\n')
        self.assertEqual(next(input_file), '|  4       | 5       | 6        |\n')
        self.assertEqual(next(input_file), '|----------+---------+----------|\n')

