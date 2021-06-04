from optimal_change import optimal_change
import unittest
    
class TestRomanNumerals(unittest.TestCase):
    """Tests for 'optimal_change.py'."""
   
    
    """ Tests for a string returned."""
    def test_returns_a_string(self):            
        self.assertTrue(type(optimal_change(5, 20)) == str)
        
    """ Tests for insufficient funds."""
    def test_returns_insufficient_funds(self):
        self.assertTrue(optimal_change(101, 100) == "You don't have enough money.")
        
    """ Tests for exact change."""
    def test_returns_if_exact_change_used(self):
        self.assertTrue(optimal_change(100, 100) == "Thank you for using exact change.  Have a nice day!")
    
    """ Tests for output accuracy."""
    def test_output_accuracy(self):        
        self.assertTrue(optimal_change(5.99, 10) == "The optimal change for an item that costs $5.99 with an amount paid of $10 is 4 $1 bills, and 1 penny.")
        self.assertTrue(optimal_change(2.43, 20) == "The optimal change for an item that costs $2.43 with an amount paid of $20 is 1 $10 bill, 1 $5 bill, 2 $1 bills, 2 quarters, 1 nickel, and 2 pennies.")
        self.assertTrue(optimal_change(22.49, 50) == "The optimal change for an item that costs $22.49 with an amount paid of $50 is 1 $20 bill, 1 $5 bill, 2 $1 bills, 2 quarters, and 1 penny.")
        
    """ Challenge questions."""
    def test_challenges(self):        
        self.assertTrue(optimal_change(110.41, 200) == "The optimal change for an item that costs $110.41 with an amount paid of $200 is 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 4 $1 bills, 2 quarters, 1 nickel, and 4 pennies.")
        self.assertTrue(optimal_change(303.01, 400) == "The optimal change for an item that costs $303.01 with an amount paid of $400 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 1 $1 bill, 3 quarters, 2 dimes, and 4 pennies.")
        

if __name__ == '__main__':
    unittest.main()
  
