from nose.tools import assert_equal, assert_greater

class TestFibSequence(object):
    def test_fib_sequence(self, func):
        assert_equal(func(None), 0)
        assert_equal(func(0), 1)
        assert_equal(func(1), 1)
        assert_equal(func(5), 13)
        assert_equal(func(-1), 0)
        assert_greater(func(100001), 100000)
        print('Success: test_fib_sequence')
        
def main():
    test = TestFibSequence()
    fib = FibSequence()
    test.test_fib_sequence(fib.value_for_n)
    
if __name__ == '__main__':
    main()