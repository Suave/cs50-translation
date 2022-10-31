from operator import is_
import unittest

def is_similar_with(name1, name2):
    if not len(name1) == len(name2):
        return False
 
    difference = 0
    for idx, chr in enumerate(name1):
        if not chr.lower() == name2[idx].lower():
            difference += 1

    if difference > 1:
        return False

    return True

class TestNameIsSimilar(unittest.TestCase):
    def test_similar(self):
        self.assertTrue(is_similar_with("Josh", "Josh"))
        self.assertTrue(is_similar_with("Alex", "alex"))
        self.assertTrue(is_similar_with("Alex", "alix"))
        self.assertTrue(is_similar_with("Sam", "CaM"))

    def test_not_similar(self):
        self.assertFalse(is_similar_with("Ann", "Anne"))
        self.assertFalse(is_similar_with("Max", "Cat"))

if __name__ == '__main__':
    unittest.main()