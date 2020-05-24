import unittest
from ProdactionCode.ArrayProcessor import ArrayProcessor


class TestArrayProcessor(unittest.TestCase):
    def setUp(self):
        self.arrayTest = [-1, -673, -1652, -51237, 0, 12, 998, 1235, 9999, 23451]
        self.arraySorted = [1235, 9999]
        self.arrayProcessor = ArrayProcessor()

    def test_sort_and_filter(self):
        arraySorted = self.arrayProcessor.sortAndFilter(self.arrayTest)
        self.assertCountEqual(arraySorted, self.arraySorted)
