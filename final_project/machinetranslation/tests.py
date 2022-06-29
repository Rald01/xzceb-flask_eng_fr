import unittest
from translator import englishToFrench
from translator import frenchToEnglish

   # Create a new file called tests.py in the machinetranslation directory.
    #Write at least 2 tests in tests.py for each method
    #Test for null input for frenchToEnglish
    #Test for null input for englishToFrench.
    #Test for the translation of the world 'Hello' and 'Bonjour'.
    #Test for the translation of the world 'Bonjour' and 'Hello'.
    #Take a screenshot of your unit tests and save it as a .jpg or .png with the filename translation_unittests.

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(frenchToEnglish(None), None)    #Test for null input for frenchToEnglish
        self.assertEqual(englishToFrench(None), None)   #Test for null input for englishToFrench

        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")    #Test for the translation of the world 'Bonjour' and 'Hello'.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")    #Test for the translation of the world 'Hello' and 'Bonjour'.


if __name__ == '__main__':
    unittest.main()
