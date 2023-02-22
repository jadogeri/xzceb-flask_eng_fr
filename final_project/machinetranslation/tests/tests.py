import unittest 
from translator import englishtofrench,frenchtoenglish

class TestNullEnglishToFrench(unittest.TestCase):
    def test1(self):
         self.assertIsNone(englishtofrench(None),None)
         
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishtofrench("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")

class TestNullFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(frenchtoenglish(None),None)

 

if __name__ == "__main__":
    unittest.main()