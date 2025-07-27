# test_futureoptima.py
"""
Tests for FutureOptima module.
"""

import unittest
from futureoptima import FutureOptima

class TestFutureOptima(unittest.TestCase):
    """Test cases for FutureOptima class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureOptima()
        self.assertIsInstance(instance, FutureOptima)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureOptima()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
