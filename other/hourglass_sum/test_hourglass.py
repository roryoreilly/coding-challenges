from nose.tools import assert_equal
import numpy as np

class TestHourGlass(object):
    def test_find_max(self, func):
        input_arr = "1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0"
        arr = []
        arr.append(list(map(int, input_arr.rstrip().split())))
        arr = np.array(arr)
        arr = arr.reshape((6, -1))
        assert_equal(func(arr), 19)
        print('Success: test_hourglass')
        
    def test_hour_glass_subset_sum(self, func):
        input_arr = "1 1 1 0 0 0 0 1 0"
        arr = []
        arr.append(list(map(int, input_arr.rstrip().split())))
        arr = np.array(arr)
        arr = arr.reshape((3, -1))
        assert_equal(func(arr), 4)
        print('Success: test_hour_glass_subset_sum')
        
def main():
    test = TestHourGlass()
    hour_glass = HourGlass()
    test.test_hour_glass_subset_sum(hour_glass.hour_glass_subset_sum)
    test.test_find_max(hour_glass.find_max)
    
if __name__ == '__main__':
    main()