from nose.tools import assert_list_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_list_equal(func([[0,2,1,0], 
                                [0,1,0,1], 
                                [1,1,0,1], 
                                [0,1,0,1]]), [2, 4, 1])
        print('Success: pond_size')
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_solution(solution.pond_sizes)
    
if __name__ == '__main__':
    main()