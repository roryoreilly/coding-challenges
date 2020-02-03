from nose.tools import assert_equal
from nose.tools import assert_not_equal

class TestSolution(object):
    def test_solution(self, deck):
        initial_deck = deck.to_list()
        assert_equal(initial_deck[0], 'Ah')
        assert_equal(len(initial_deck), 52)
        
        deck.shuffle()
        shuffle_deck = deck.to_list()
        assert_not_equal(shuffle_deck[0], 'Ah')
        assert_not_equal(initial_deck, shuffle_deck)
        print('Success: shuffle_deck')
        
def main():
    test = TestSolution()
    deck = Deck()
    test.test_solution(deck)
    
if __name__ == '__main__':
    main()