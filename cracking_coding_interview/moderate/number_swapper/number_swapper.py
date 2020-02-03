from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func([1,2,3], 0, 2), [3,2,1])
        assert_equal(func([1,2,3], 1, 0), [2,1,3])
        print('Success: number_swapper')
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_solution(solution.number_swapper)
    
if __name__ == '__main__':
    main()