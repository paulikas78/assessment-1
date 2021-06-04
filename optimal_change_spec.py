from optimal_change import optimal_change
import unittest
    
class TestOptimalChange(unittest.TestCase):
    """Tests for 'optimal_change.py'."""
   
    
    """ Tests for a string returned."""
    def test_returns_a_string(self):            
        self.assertTrue(type(optimal_change(5, 20)) == str)
        
    """ Tests for insufficient funds."""
    def test_returns_insufficient_funds(self):
        self.assertTrue(optimal_change(101, 100) == "Insufficient funds.  Please add money to make a purchase.")
        
    """ Tests for exact change."""
    def test_returns_if_exact_change_used(self):
        self.assertTrue(optimal_change(100, 100) == "Thank you for using exact change.  Have a nice day!")
    
    """ Tests for output accuracy."""
    def test_output_accuracy(self):        
        self.assertTrue(optimal_change(5.47, 10) == "The optimal change for an item that costs $5.47 with an amount paid of $10 is 4 $1 bills, 2 quarters, and 3 pennies.")
        self.assertTrue(optimal_change(2.43, 20) == "The optimal change for an item that costs $2.43 with an amount paid of $20 is 1 $10 bill, 1 $5 bill, 2 $1 bills, 2 quarters, 1 nickel, and 2 pennies.")
        self.assertTrue(optimal_change(22.49, 50) == "The optimal change for an item that costs $22.49 with an amount paid of $50 is 1 $20 bill, 1 $5 bill, 2 $1 bills, 2 quarters, and 1 penny.")
        
    """ Challenge questions."""
    def test_challenge_questions(self):        
        self.assertTrue(optimal_change(122.44, 200) == "The optimal change for an item that costs $122.44 with an amount paid of $200 is 1 $50 bill, 1 $20 bill, 1 $5 bill, 2 $1 bills, 2 quarters, 1 nickel, and 1 penny.")
        self.assertTrue(optimal_change(2.26, 100) == "The optimal change for an item that costs $2.26 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 2 $1 bills, 2 quarters, 2 dimes, and 4 pennies.")
        
if __name__ == '__main__':
    unittest.main()
  
