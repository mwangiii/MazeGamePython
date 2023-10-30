import unittest
from maze import sequence, contains, add, remove, neighbors
from laby import laby

class TestMazeFunctions(unittest.TestCase):
    """tests for maze.py"""

    def test_sequence(self):
        """Test case for sequence function"""
        result = sequence(5) 
        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_contains(self):
        """Test case for contains function - positive case"""
        result_positive = contains([1, 2, 3], 2)
        self.assertTrue(result_positive)

        """Test case for contains function - negative case"""
        result_negative = contains([1, 2, 3], 4)
        self.assertFalse(result_negative)

    def test_add(self):
        """Test case for add function"""
        result = add([9, 2, 5], 2) 
        self.assertEqual(result, [9, 2, 5])

    def test_remove(self):
        """Test case for remove function"""
        result = remove([1, 2, 3], 2)
        self.assertEqual(result, [1, 3])

    def test_neighbors(self):
        """Test case for neighbors function"""
        result = neighbors(7, 2, 8, 4)
        self.assertEqual(result, [15, 22, 31])


    # this fuction is not working
    def test_laby(self):
        """
        Test case for laby procedure
        Since laby involves visual output, you can test if it runs without errors
        """
        # Test with valid parameters
        try:
            laby(16, 9, 20)
        except Exception as e:
            self.fail(f"laby(16, 9, 20) raised an exception: {str(e)}")

        # Test with invalid parameters (e.g., negative values)
        with self.assertRaises(Exception):
            laby(-3, 3, 2)

if __name__ == "__main__":
    unittest.main()
