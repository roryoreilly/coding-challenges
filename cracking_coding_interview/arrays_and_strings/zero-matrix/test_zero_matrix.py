from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func([[0,1],[1,2],[2,1]]), [[0,0],[0,2],[0,1]])
        assert_equal(func([[1,1],[1,2],[2,1]]), [[1,1],[1,2],[2,1]])
        assert_equal(func([[0,1],[1,2],[0,1]]), [[0,0],[0,2],[0,0]])
        print('Success: test_zero_matrix')
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_solution(solution.zero_matrix)
    test.test_solution(solution.zero_matrix_df)
    
if __name__ == '__main__':
    main()