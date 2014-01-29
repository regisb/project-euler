from collections import defaultdict

def card_value(value):
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value == "K":
        return 13
    if value == "A":
        return 14
    if value == "T":
        return 10
    return int(value)

def compare_scores(score1, score2):
    if score1[0] > score2[0]:
        return 1
    if score1[0] < score2[0]:
        return -1
    for value1, value2 in zip(score1[1], score2[1]):
        if value1 > value2:
            return 1
        if value1 < value2:
            return 61
    return 0

class Card(object):
    def __init__(self, card_string):
        self.value = card_value(card_string[0])
        self.color = card_string[1]

    def __lt__(self, card):
        return self.value < card.value

    def __repr__(self):
        return "%2d-%s" % (self.value, self.color)

class Hand(object):
    def __init__(self, string_representation):
        card_strings = string_representation.split(" ")
        #print card_strings
        self.cards = sorted([Card(card_string) for card_string in card_strings])

    def different_card_count(self):
        return len(set([card.value for card in self.cards]))

    def beats(self, hand):
        score1 = self.combination_score()
        score2 = hand.combination_score()
        return compare_scores(score1, score2) == 1

    def combination_score(self):
        score = self.straight_flush()
        if score is not None:
            return score
        score = self.four_of_a_kind()
        if score is not None:
            return score
        score = self.full_house()
        if score is not None:
            return score
        score = self.flush()
        if score is not None:
            return score
        score = self.straight()
        if score is not None:
            return score
        score = self.three_of_a_kind()
        if score is not None:
            return score
        score = self.two_pairs()
        if score is not None:
            return score
        score = self.one_pair()
        if score is not None:
            return score
        score = self.high_card()
        if score is not None:
            return score

    def assert_different_card_count(self, count):
        if self.different_card_count() != count:
            print "HOUSTON!", self.cards

    def straight_flush(self):
        if self.flush() is None or self.straight() is None:
            return None
        self.assert_different_card_count(5)
        return (9, [self.cards[4].value])

    def four_of_a_kind(self):
        groups = self.value_groups()
        if 4 not in groups:
            return None
        self.assert_different_card_count(2)
        return (8, [groups[4][0], groups[1][0]])

    def full_house(self):
        groups = self.value_groups()
        if 3 not in groups or 2 not in groups:
            return None
        self.assert_different_card_count(2)
        return (7, [groups[3][0], groups[2][0]])

    def flush(self):
        color = self.cards[0].color
        for card in self.cards:
            if card.color != color:
                return None
        self.assert_different_card_count(5)
        return (6, self.highest_card_values())

    def straight(self):
        card_values = self.highest_card_values()
        highest_card_value = card_values[0]
        if card_values != range(highest_card_value, highest_card_value - 5, -1):
            return None
        self.assert_different_card_count(5)
        return (5, [highest_card_value])

    def three_of_a_kind(self):
        groups = self.value_groups()
        if 3 not in groups:
            return None
        remaining_cards = sorted(groups[1], reverse=True)
        self.assert_different_card_count(3)
        return (4, [groups[3][0]] + remaining_cards)

    def two_pairs(self):
        groups = self.value_groups()
        if 2 not in groups or len(groups[2]) != 2:
            return None
        pair_values = sorted(groups[2], reverse=True)
        remaining_card = groups[1][0]
        self.assert_different_card_count(3)
        return (3, pair_values + [remaining_card])

    def one_pair(self):
        groups = self.value_groups()
        if 2 not in groups:
            return None
        remaining_cards = sorted(groups[1], reverse=True)
        self.assert_different_card_count(4)
        return (2, [groups[2][0]] + remaining_cards)

    def high_card(self):
        self.assert_different_card_count(5)
        return (1, self.highest_card_values())

    def highest_card_values(self):
        return sorted([card.value for card in self.cards], reverse=True)

    def value_groups(self):
        """value_groups
        Return the card values indexed by their number of appearances. E.g a
        four-of-a-kind of 6 with an additional 7 produces the following result:
            {4: [6], 1: [7] }
        """
        value_count = defaultdict(int)
        for card in self.cards:
            value_count[card.value] += 1
        value_groups = defaultdict(list)
        for value, count in value_count.iteritems():
            value_groups[count].append(value)
        return value_groups

class Game(object):
    def __init__(self, string_representation):
        self.hand1 = Hand(string_representation[:14])
        self.hand2 = Hand(string_representation[15:])

    def winner(self):
        if self.hand1.beats(self.hand2):
            return 1
        else:
            # Note that we don't care for ties
            return 2

def game_winner(line):
    game = Game(line.strip())
    return game.winner()

def count_player1_victories(path):
    count = 0
    with open(path) as f:
        for line in f:
            if game_winner(line) == 1:
                count += 1
    return count

import unittest
class Test(unittest.TestCase):
    def assert_beats(self, score1, score2):
        self.assertEqual(1, compare_scores(score1, score2))

    def assert_does_not_beat(self, score1, score2):
        self.assertNotEqual(1, compare_scores(score1, score2))

    def test_cards_are_sorted(self):
        hand = Hand("4H 5H 6H 8H 7H")
        self.assertEqual(8, hand.cards[4].value)

    def test_compare_scores(self):
        self.assert_beats((2, [1, 2]), (1, [4, 5]))
        self.assert_beats((5, [1, 2]), (5, [1, 1]))
        self.assert_does_not_beat((2, [3, 4]), (2, [3, 4]))
        self.assert_does_not_beat((2, [3, 4]), (2, [4, 4]))

    def assert_hand_beats(self, string1, string2):
        hand1 = Hand(string1)
        hand2 = Hand(string2)
        self.assertTrue(hand1.beats(hand2))

    def test_straight_flush(self):
        hand = Hand("4H 5H 6H 8H 7H")
        self.assertIsNotNone(hand.flush())
        self.assertIsNotNone(hand.straight())
        score = hand.combination_score()
        self.assertEqual((9, [8]), score)

    def test_hands(self):
        self.assert_hand_beats("4H 5H 6H 8H 7H", "TH TD TC KD TS")

if __name__ == "__main__":
    #unittest.main()
    print count_player1_victories("poker.txt")
