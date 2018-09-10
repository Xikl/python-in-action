#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 12:03
# @Author  : 朱文赵
# @Site    : 
# @File    : french_deck.py
# @Software: PyCharm

import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[0])
    # print(deck[51])
    # # 随机选择
    # choice(deck)
    #
    # # 切片
    # # 获得前三个
    # print(deck[:3])
    # # 隔13张拿12的那一张
    # print(deck[12::13])
    #
    # # __getitem__方法，这一摞牌就变成可迭代的了：
    # for card in deck:  # doctest: +ELLIPSIS
    #     print(card)
    #
    # print(Card('Q', 'hearts') in deck)

    # for card in sorted(deck, key=spades_high):
    #     print(card)

