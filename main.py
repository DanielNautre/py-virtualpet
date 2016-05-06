#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pet
import ui


class virtualPet(object):
    """docstring for virtualPet"""
    def __init__(self, arg):
        super(virtualPet, self).__init__()
        self.arg = arg

        # Create the window and the UI
        self.window = ui.UI(None)
        self.window.createMainWindow()
        self.window.drawUserInterface()

        # create the pet and draw it
        self.pet = pet.Pet(None)
        self.window.drawPet(self.pet)

    def computeTick(self):
        """ compute all action to be done on each game tick (1 second)"""
        if self.pet.hunger == 0 and self.pet.health > 0:
            self.pet.health = self.pet.health - 1
        if self.pet.hunger > 0:
            self.pet.hunger = self.pet.hunger - 0.1

        if self.pet.health == 0:
            self.pet.alive = False


if __name__ == "__main__":

    game = virtualPet(None)

    while game.window.isAlive:

        game.window.setTickSpeed(1)  # n frames per second

        # Handle user input, then compute passing time, then redraw game
        game.window.handleEvent(game.pet)
        game.computeTick()
        game.window.redraw(game.pet)

        # print "hunger: %.1f" % (game.pet.hunger, )
        print "health: %.1f" % (game.pet.health, )
