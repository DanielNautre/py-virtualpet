#!/usr/bin/python2.7
# -*- coding: utf8 -*

from collections import defaultdict
import moodlets as m


class Pet(object):
    """docstring for Pet"""

    MAXHUNGER = 100
    MAXBLADER = 100

    def __init__(self, arg):
        super(Pet, self).__init__()
        self.arg = arg
        self.initializeValues()

    def initializeValues(self):
        """ set values when the pet is born"""

        self.age = 0  # age in gametick
        self.hunger = 100  # how hungry is the pet
        self.health = 100  # how healthy is the pet
        self.love = 0  # how much does your pet love you
        self.blader = 0  # does you'r pet have a pressing need ?
        self.dirt = 0  # how dirty your pet is
        self.alive = True
        self.activeMood = defaultdict(list)
        self.name = ""

    def setName(self, value):
        self.name = value

    def feed(self):
        self.hunger = min(self.hunger + 50, Pet.MAXHUNGER)
        self.blader = min(self.blader + 25, Pet.MAXBLADER)
        self.activeMood["fed"].append(m.moodlets["fed"]["duration"])

    def heal(self):
        self.health = min(self.health + 50, 100)

    def clean(self):
        self.dirt = 0
        del self.activeMood["dirty"]

    def moodletDecrease(self):
        markedfordeletion = []
        y = 0
        for mood in self.activeMood.iteritems():
            i = 0
            for duration in mood[1]:
                # decrease time on all moodlets
                self.activeMood[mood[0]][i] = duration - 1

                # if moodlet has -1 duration, it never expires
                if self.activeMood[mood[0]][i] == -1:
                    continue
                # if moodlet has 0 time, remove it
                if self.activeMood[mood[0]][i] < 1:
                    del self.activeMood[mood[0]][i]

                if len(self.activeMood[mood[0]]) == 0:
                    markedfordeletion.append(mood[0])

                i = i + 1
                y = y + 1

        # if all instances of a moodlets have expired, remove it from the list
        for marked in markedfordeletion:
            del self.activeMood[marked]

    def getCurrentMood(self):
        moodValue = 50

        for mood in self.activeMood.iteritems():
            if m.moodlets[mood[0]]["stackable"]:
                stacksize = m.moodlets[mood[0]]["stackable"]
                toadd = len(mood[1]) * m.moodlets[mood[0]]["value"]
                moodValue = moodValue + min(toadd, stacksize)
            else:
                moodValue = moodValue + m.moodlets[mood[0]]["value"]

        return moodValue

    def addMood(self, mood):
        self.activeMood[mood].append(m.moodlets[mood]["duration"])
