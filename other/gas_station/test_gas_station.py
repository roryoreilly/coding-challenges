from nose.tools import assert_equal

class TestGasStation(object):
    def test_minimum_stating_gas(self, func):
        assert_equal(func([1, 2], [2, 1]), 1)
        assert_equal(func([1, 1, 1], [2, 2, 2]), -1)
        assert_equal(func([1, 1, 3], [2, 2, 1]), 2)
        print('Success: test_minimum_stating_gas')
        
    def test_single_gas_trip(self, func):
        assert_equal(func([2, 1], [1, 2]), 0)
        assert_equal(func([1, 1, 1], [2, 2, 2]), -1)
        print('Success: test_single_gas_trip')
        
def main():
    test = TestGasStation()
    gas_station = GasStation()
    test.test_single_gas_trip(gas_station.gas_for_trip)
    test.test_minimum_stating_gas(gas_station.minimum_stating_gas)
    
if __name__ == '__main__':
    main()