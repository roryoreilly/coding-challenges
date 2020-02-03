from nose.tools import assert_equal

class TestSolution(object):
    def test_solution(self, func):
        assert_equal(func(5000), 0)
        assert_equal(func(15000), 500)
        assert_equal(func(25000), 2000)
        assert_equal(func(40000), 6000)
        print('Success: calculate_tax')
        
def main():
    test = TestSolution()
    tax_cal = TaxCalculator([[10000, .1],[20000, .2], [30000, .3], [None, 0]])
    test.test_solution(tax_cal.calcuate)
    
if __name__ == '__main__':
    main()