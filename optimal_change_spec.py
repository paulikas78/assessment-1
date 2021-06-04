from roman_numerals import to_roman
import unittest
    
class TestRomanNumerals(unittest.TestCase):
    """Tests for 'roman_numerals.py'."""
    #add 2 more tests
    
    """ Tests for a string returned."""
    def test_returns_a_string(self):            
        self.assertTrue(type(to_roman(5)) == str)
    
    """ Tests for output accuracy."""
    def test_output_accuracy(self):        
        self.assertTrue(to_roman(1) == "I")
        self.assertTrue(to_roman(8) == "VIII")
        self.assertTrue(to_roman(54) == "LIV")
        self.assertTrue(to_roman(219) == "CCXIX")
        
    """ Challenge questions."""
    def test_challenges(self):        
        self.assertTrue(to_roman(2021) == "MMXXI")
        self.assertTrue(to_roman(777) == "DCCLXXVII")
        self.assertTrue(to_roman(939) == "CMXXXIX")
        self.assertTrue(to_roman(94) == "XCIV")

if __name__ == '__main__':
    unittest.main()
  
