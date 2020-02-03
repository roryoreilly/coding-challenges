from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func("world"), 2)
        assert_equal(func("non"), 0)
        assert_equal(func("hello"), 1)
        print('Success: word_frequency')
        
def main():
    test = TestSolution()
    solution = Solution("hello world how are you world")
    test.test_solution(solution.get_count)
    
if __name__ == '__main__':
    main()