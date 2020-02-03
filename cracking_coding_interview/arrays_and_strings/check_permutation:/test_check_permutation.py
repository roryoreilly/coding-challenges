from nose.tools import assert_equal

class TestSolution:
    def test_solution(self, func):
        assert_equal(func(None, None), False)
        assert_equal(func('abc', 'cab'), True)
        assert_equal(func('abac', 'cab'), False)
        assert_equal(func('ab', 'cab'), False)
        assert_equal(func('abac', 'caba'), True)
        print("Successful: check_permutations")
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_solution(solution.check_permutation)
    
if __name__ == '__main__':
    main()