#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pet
import ui

import time


class virtualPet(object):
    """docstring for virtualPet"""
    def __init__(self, arg):
        super(virtualPet, self).__init__()
        self.arg = arg
        self.window = ui.UI(None)
        self.window.createMainWindow()
        self.createPet()

    def computeTick(self):
        """ compute all action to be done on each game tick (1 second)"""
        if self.pet.hunger == 0:
            self.pet.health = self.pet.health - 1
        if self.pet.hunger > 0:
            self.pet.hunger = self.pet.hunger - 0.1

        if self.pet.health == 0:
            self.pet.alive = False
        pass

    def createPet(self):
        self.pet = pet.Pet(None)


if __name__ == "__main__":

    game = virtualPet(None)

    while game.window.isAlive:

        game.window.handleEvent()
        game.computeTick()

        time.sleep(1)
        pass

    # create the window
    # create the pet
    # run the mainloop
