import unittest
from translator import englishtofrench
from translator import frenchtoenglish

class Test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishtofrench('Hello'),'Hello')
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtofrench("None"), '')
        self.assertNotEqual(englishtofrench(0), 0)

class Test_frenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Bonjour')
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchtoenglish("None"), '')
        self.assertNotEqual(frenchtoenglish(0), 0)
    

unittest.main()
    