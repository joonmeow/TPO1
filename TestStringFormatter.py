import unittest, os
from ProdactionCode.StringFormatter import StringFormatter


class TestStringFormatter(unittest.TestCase):
    def setUp(self):
        self.stringFormatter = StringFormatter()
        self.pathTest = 'D:\\test.txt'
        self.pathTestWithoutExt = 'D:\\test'
        self.pathFormatted = 'TEST.TMP'
        self.null = None
        self.emptyString = ''
        self.noPath = 'qddqwqwd:xa::?'
        open(self.pathTest, 'a').close()
        open(self.pathTestWithoutExt, 'a').close()

    def tearDown(self):
        os.remove(self.pathTest)
        os.remove(self.pathTestWithoutExt)

    def test_short_format(self):
        pathFormatted = self.stringFormatter.shortFileString(self.pathTest)
        self.assertEqual(pathFormatted, self.pathFormatted)

    def test_short_format_without_ext(self):
        pathFormatted = self.stringFormatter.shortFileString(self.pathTestWithoutExt)
        self.assertEqual(pathFormatted, self.pathFormatted)

    def test_null_short_format_file(self):
        pathFormatted = self.stringFormatter.shortFileString(self.null)
        self.assertEqual(self.null, pathFormatted)

    def test_empty_short_format_file(self):
        pathFormatted = self.stringFormatter.shortFileString(self.emptyString)
        self.assertEqual(self.emptyString, pathFormatted)

    @unittest.expectedFailure
    def test_no_path_short_format_file(self):
        self.assertRaises(ValueError, self.stringFormatter.shortFileString(self.noPath))
