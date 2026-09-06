# test_sampleember.py
"""
Tests for SampleEmber module.
"""

import unittest
from sampleember import SampleEmber

class TestSampleEmber(unittest.TestCase):
    """Test cases for SampleEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SampleEmber()
        self.assertIsInstance(instance, SampleEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SampleEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
