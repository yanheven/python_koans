#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.
import itertools
import random

from runner.koan import *


class DiceSet(object):
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        self._values = [random.randint(1,6) for i in range(n)]

def score(dice):
    # You need to write this method
    dice = sorted(dice)
    point = 0
    dice_group = itertools.groupby(dice)
    for k, v in dice_group:
        length = len(list(v))
        if length>2:
            if k == 1:
                point += 1000 + 100 * (length -3)
            else:
                point += k*100
            if k == 5:
                point += 50 * (length-3)
        elif k == 1:
            point += 100 * length
        elif k == 5:
            point += 50 * length
    return point

class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass
