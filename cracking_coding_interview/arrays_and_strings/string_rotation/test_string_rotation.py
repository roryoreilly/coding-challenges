from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func(None, None), False)
        assert_equal(func('waterbottle', 'erbottlewat'), True)
        assert_equal(func('a', 'a'), True)
        assert_equal(func('a', 'ab'), False)
        assert_equal(func('waterbottle', 'terbottlwae'), False)
        print('Success: test_string_rotation')
        
    def test_rotation(self, func):
        assert_equal(func("hello"), "elloh")
        print('Success: test_rotate_a_string')
        
def main():
    test = TestSolution()
    solution = Solution()
    test.test_rotation(solution.rotate)
    test.test_solution(solution.is_substring)
    
if __name__ == '__main__':
    main()