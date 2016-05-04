#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame


class UI(object):
    """UI Class, handles all UI related stuff"""

    WINSIZE = (800, 600)

    def __init__(self, arg):
        super(UI, self).__init__()
        self.arg = arg
        pygame.init()

    def initiateMainValues(self):
        # Feed Button
        self.feedBtnSize = (50, 50)
        self.feedBtnPos = (150, 150)
        self.feedBtnPath = "assets/img/feedBtn.png"

        # Heal Button
        self.healBtnSize = (50, 50)
        self.healBtnPos = (150, 200)
        self.healBtnPath = "assets/img/healBtn.png"

    def loadImages(self):
        """Load images into memory"""

        # Load the background
        self.background = pygame.image.load("assets/img/background.png")
        self.background = self.background.convert()

        # Load Pet images
        self.aliveImg = pygame.image.load("assets/img/live-pet.png")
        self.aliveImg = self.aliveImg.convert_alpha()

        self.deadImg = pygame.image.load("assets/img/dead-pet.png")
        self.deadImg = self.deadImg.convert_alpha()

        # Load UI elements
        self.feedBtnImg = pygame.image.load(self.feedBtnPath)
        self.feedBtnImg = self.feedBtnImg.convert_alpha()

        self.healBtnImg = pygame.image.load(self.healBtnPath)
        self.healBtnImg = self.healBtnImg.convert_alpha()


    def createMainWindow(self):

        self.initiateMainValues()

        # create game window
        self.window = pygame.display.set_mode(UI.WINSIZE)

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
                btnStartX = self.feedBtnPos[0]
                btnStopX = self.feedBtnPos[0] + self.feedBtnSize[0]

                btnStartY = self.feedBtnPos[1]
                btnStopY = self.feedBtnPos[1] + self.feedBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.feed()
                    continue

                # Heal ?
                btnStartX = self.healBtnPos[0]
                btnStopX = self.healBtnPos[0] + self.healBtnSize[0]

                btnStartY = self.healBtnPos[1]
                btnStopY = self.healBtnPos[1] + self.healBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.heal()
                    continue

    def drawBackground(self):
        self.window.blit(self.background, (0, 0))

    def drawUserInterface(self):
        self.window.blit(self.feedBtnImg, self.feedBtnPos)
        self.window.blit(self.healBtnImg, self.healBtnPos)

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
