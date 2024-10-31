import unittest

def sortArray(array):
    for i in range( len(array)-1):
        for j in range( len(array)-i-1):
            if abs(array[j]) < abs(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

class TestMyFunction(unittest.TestCase):
    firstArr=[1,4,5,7,34,3,32,782]
    secondArr=[-1,-3,-4,-5,-7,-34,-32,-782]
    thirdArr=[1,2,-3,4,-45,23,-12,8,-5]
    def test_sort_positive_numbers(self):
        self.assertEqual(sortArray(self.firstArr),[782,34,32,7,5,4,3,1])
    def test_sort_negative_numbers(self):
        self.assertEqual(sortArray(self.secondArr),[-782,-34,-32,-7,-5,-4,-3,-1])
    def test_sort_different_numbers(self):
        self.assertEqual(sortArray(self.thirdArr),[-45,23,-12,8,-5,4,-3,2,1])

if __name__ == '__main__':
    unittest.main()
    