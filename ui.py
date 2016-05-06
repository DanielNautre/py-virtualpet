#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame
import uisettings as uis


class UI(object):
    """UI Class, handles all UI related stuff"""

    def __init__(self, arg):
        super(UI, self).__init__()
        self.arg = arg
        pygame.init()

    def loadImages(self):
        """Load images into memory"""

        # Load the background
        self.background = pygame.image.load(uis.backgroundImgPath).convert()

        # Load Pet images
        self.aliveImg = pygame.image.load(uis.aliveImgPath).convert_alpha()
        self.deadImg = pygame.image.load(uis.deadImgPath).convert_alpha()

        # Load UI elements
        self.feedBtnImg = pygame.image.load(uis.feedBtnPath).convert_alpha()
        self.healBtnImg = pygame.image.load(uis.healBtnPath).convert_alpha()

    def createMainWindow(self):
        # create game window
        self.window = pygame.display.set_mode(uis.WINSIZE)

        # load images into memory
        self.loadImages()

        self.isAlive = True

    def handleEvent(self, pet):
        """define action to be taken depending on user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isAlive = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos[0], event.pos[1]

                # print "X = %d & Y= %d" % (x, y)

                # Feed ?
                btnStartX = uis.feedBtnPos[0]
                btnStopX = uis.feedBtnPos[0] + uis.feedBtnSize[0]

                btnStartY = uis.feedBtnPos[1]
                btnStopY = uis.feedBtnPos[1] + uis.feedBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.feed()
                    continue

                # Heal ?
                btnStartX = uis.healBtnPos[0]
                btnStopX = uis.healBtnPos[0] + uis.healBtnSize[0]

                btnStartY = uis.healBtnPos[1]
                btnStopY = uis.healBtnPos[1] + uis.healBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.heal()
                    continue

    def drawBackground(self):
        self.window.blit(self.background, (0, 0))

    def drawUserInterface(self):
        self.window.blit(self.feedBtnImg, uis.feedBtnPos)
        self.window.blit(self.healBtnImg, uis.healBtnPos)

    def drawPet(self, pet):
        if pet.alive is True:
            self.window.blit(self.aliveImg, (200, 300))
        else:
            self.window.blit(self.deadImg, (200, 300))

    def redraw(self, pet):
        self.drawBackground()
        self.drawPet(pet)
        self.drawUserInterface()

        pygame.display.flip()

    def setTickSpeed(self, value):
        pygame.time.Clock().tick(value)
