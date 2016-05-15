#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pet
import ui
import starter


class virtualPet(object):
    """docstring for virtualPet"""
    def __init__(self, arg):
        super(virtualPet, self).__init__()
        self.arg = arg

        # create the pet and draw it
        self.pet = pet.Pet(None)

        # Create the window and the UI
        self.window = ui.UI(None)
        self.window.createMainWindow()
        self.window.drawUserInterface(self.pet)
        self.window.drawPet(self.pet)

    def computeTick(self):
        """ compute all action to be done on each game tick (1 second)"""

        self.pet.moodletDecrease()

        if self.pet.hunger == 0 and self.pet.health > 0:
            self.pet.health = self.pet.health - 1
        if self.pet.hunger > 0:
            self.pet.hunger = self.pet.hunger - 0.1

        if self.pet.blader > 80:
            self.pet.dirt = self.pet.dirt + 50
            self.pet.blader = 0

        if self.pet.dirt > 80:
            self.pet.addMood("dirty")

        if self.pet.health == 0:
            self.pet.alive = False


if __name__ == "__main__":

    # create a window to choose the pet's name
    starter = starter.starter(None)
    starter.title('Virtual Pet: start')
    starter.mainloop()

    # once the loop finishes (the starter window is closed),
    # launch the actual game

    game = virtualPet(None)
    game.pet.setName(starter.name)

    while game.window.isAlive:

        game.window.setTickSpeed(1)  # n frames per second

        # Handle user input, then compute passing time, then redraw game
        game.window.handleEvent(game.pet)
        game.computeTick()
        game.window.redraw(game.pet)

        print "------------------------------------------"
        # print "hunger: %.1f" % (game.pet.hunger, )
        # print "health: %.1f" % (game.pet.health, )
        print "blader: %.1f " % (game.pet.blader, )
        print "dirt: %.1f " % (game.pet.dirt, )
        # print "mood: %d " % (game.pet.getCurrentMood(), )
        print "moodlets: "
        print game.pet.activeMood
