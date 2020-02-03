from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func(2, 5, 3), [10, 8, 6])
        assert_equal(func(3, 5, 3), [15, 13, 11, 9])
        assert_equal(func(4, 5, 3), [20, 18, 16, 14, 12])
        print('Success: example_notebook')
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_solution(solution.solution)
    test.test_solution(solution.solution2)
    
if __name__ == '__main__':
    main()