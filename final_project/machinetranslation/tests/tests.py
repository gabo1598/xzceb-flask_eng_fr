import unittest
import translator

class Test1(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') 
        self.assertEqual(translator.english_to_french(''), 'Bonjour') 


class Test2(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') 
        self.assertEqual(translator.french_to_english(''), 'Hello') 
        
unittest.main()