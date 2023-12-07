#!/usr/bin/env python3

import sys

USE_JOKER = False

def is_5_of_a_kind(cards):
    if USE_JOKER:
        jokers = cards.count('J')
        if jokers == 5:
            return True
        card = cards[0]
        count = 1
        while card == 'J' and count < len(cards):
            card = cards[count]
            count += 1
        return 5 == jokers + cards.count(card)
    return 5 == cards.count(cards[0])

def is_4_of_a_kind(cards):
    if USE_JOKER:
        jokers = cards.count('J')
        for card in cards:
            if card != 'J' and 4 == jokers + cards.count(card):
                return True
        return False
    return 4 == cards.count(cards[0]) or 4 == cards.count(cards[1])

def is_fullhouse(cards):
    if USE_JOKER:
        jokers = cards.count('J')
        if jokers > 1:
            return False   # should be higher up
        if jokers == 1:   # check for 2 pairs
            for card in cards:
                if card != 'J' and cards.count(card) != 2:
                    return False
            return True
    type1 = cards[0]
    type2 = cards[0]
    count = 0
    while type1 == type2:
        type2 = cards[count]
        count += 1
    return 2 == cards.count(type1) and 3 == cards.count(type2) or 3 == cards.count(type1) and 2 == cards.count(type2)

def is_3_of_a_kind(cards):
    if USE_JOKER:
        jokers = cards.count('J')
        if jokers > 1:
            return True
        if jokers == 1:   # check for pair
            for card in cards:
                if cards.count(card) == 2:
                    return True
    for i in range(3):
        if 3 == cards.count(cards[i]):
            return True
    return False

def is_2_pairs(cards):
    if USE_JOKER:
        jokers = cards.count('J')
        if jokers >= 1:
            return False # if there was a single pair, 3oak would be higher
            # if there is no pair, 2 J needed -> also 3oak
    type1 = cards[0]
    type2 = cards[0]
    count = 0
    while type1 == type2 and count < len(cards):
        type2 = cards[count]
        count += 1
    type3 = type2
    while (type2 == type3 or type1 == type3) and count < len(cards):
        type3 = cards[count]
        count += 1
    count1 = cards.count(type1)
    count2 = cards.count(type2)
    count3 = cards.count(type3)
    return 2 == count1 and 2 == count2 or 2 == count1 and 2 == count3 or 2 == count2 and 2 == count3

def is_pair(cards):
    if USE_JOKER:
        if cards.count('J') >= 1: # if there is a single joker, a pair is present
            return True
        # has to be highest because of order
    for i in range(4):
        if 2 == cards.count(cards[i]):
            return True
    return False

def card_to_value(card):
    if card == 'A':
        return 14
    if card == 'K':
        return 13
    if card == 'Q':
        return 12
    if card == 'J':
        if USE_JOKER:
            return 1
        return 11
    if card == 'T':
        return 10
    return int(card)

def cmp_single_card(card1, card2):
    card1 = card_to_value(card1)
    card2 = card_to_value(card2)
    if card1 > card2:
        return 1
    if card2 > card1:
        return -1
    return 0

def cmp_cards(c1, c2):
        for i in range(len(c1)):
            comp = cmp_single_card(c1[i], c2[i])
            if comp != 0: return comp
        return 0

def cmp_sets(c1, c2):
    set1 = c1[0]
    set2 = c2[0]
    if set1 == set2:
        return 0
    if is_5_of_a_kind(set1) and is_5_of_a_kind(set2):
        return cmp_cards(set1, set2)
    if is_5_of_a_kind(set1):
        return 1
    if is_5_of_a_kind(set2):
        return -1
    if is_4_of_a_kind(set1) and is_4_of_a_kind(set2):
        return cmp_cards(set1, set2)
    if is_4_of_a_kind(set1):
        return 1
    if is_4_of_a_kind(set2):
        return -1
    if is_fullhouse(set1) and is_fullhouse(set2):
        return cmp_cards(set1, set2)
    if is_fullhouse(set1):
        return 1
    if is_fullhouse(set2):
        return -1
    if is_3_of_a_kind(set1) and is_3_of_a_kind(set2):
        return cmp_cards(set1, set2)
    if is_3_of_a_kind(set1):
        return 1
    if is_3_of_a_kind(set2):
        return -1
    if is_2_pairs(set1) and is_2_pairs(set2):
        return cmp_cards(set1, set2)
    if is_2_pairs(set1):
        return 1
    if is_2_pairs(set2):
        return -1
    if is_pair(set1) and is_pair(set2):
        return cmp_cards(set1, set2)
    if is_pair(set1):
        return 1
    if is_pair(set2):
        return -1
    return cmp_cards(set1, set2)


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


if __name__ == '__main__':
    data = [line.strip('\n').split(' ') for line in open(sys.argv[1])]
    res1, res2 = 0, 0

    data.sort(key=cmp_to_key(cmp_sets))
    for i in range(len(data)):
        res1 += (i + 1) * int(data[i][1])

    print("Result Challenge 1: " + str(res1))

    USE_JOKER = True
    data.sort(key=cmp_to_key(cmp_sets))
    for i in range(len(data)):
        res2 += (i + 1) * int(data[i][1])
    # for d in data:
        # print(d[0])
    print("Result Challenge 2: " + str(res2))
