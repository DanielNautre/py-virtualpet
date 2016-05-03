#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame


class UI(object):
    """UI Class, handles all UI related stuff"""

    WINSIZE = (640, 480)

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

    def createMainWindow(self):

        self.initiateMainValues()

        # create game window
        self.window = pygame.display.set_mode(UI.WINSIZE)

        # create background and stick it on the window
        self.background = pygame.image.load("assets/img/background.png")
        self.background = self.background.convert()

        self.window.blit(self.background, (0, 0))

        self.isAlive = True

    def createUserInterface(self):
        # Create Feed Button
        self.feedBtnImg = pygame.image.load(self.feedBtnPath)
        self.feedBtnImg = self.feedBtnImg.convert_alpha()
        self.window.blit(self.feedBtnImg, self.feedBtnPos)

        # Create Heal Button
        self.healBtnImg = pygame.image.load(self.healBtnPath)
        self.healBtnImg = self.healBtnImg.convert_alpha()
        self.window.blit(self.healBtnImg, self.healBtnPos)

    def handleEvent(self, pet):
        """define action to be taken depending on user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isAlive = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos[0], event.pos[1]

                # Feed ?
                btnStartX = self.feedBtnPos[0]
                btnStopX = self.feedBtnPos[0] + self.feedBtnSize[0]

                btnStartY = self.feedBtnPos[1]
                btnStopY = self.feedBtnPos[1] + self.feedBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.feed()
                else:
                    continue

                # Heal ?
                btnStartX = self.healBtnPos[0]
                btnStopX = self.healBtnPos[0] + self.healBtnSize[0]

                btnStartY = self.healBtnPos[1]
                btnStopY = self.healBtnPos[1] + self.healBtnSize[1]

                if (btnStartX < x < btnStopX and
                        btnStartY < y < btnStopY):
                    pet.heal()
                else:
                    continue


    def showPet(self, pet):
        if pet.alive is True:
            self.petImg = pygame.image.load("assets/img/live-pet.png")
            self.petImg = self.petImg.convert_alpha()
            self.window.blit(self.petImg, (200, 300))
        else:
            self.petImg = pygame.image.load("assets/img/dead-pet.png")
            self.petImg = self.petImg.convert_alpha()
            self.window.blit(self.petImg, (200, 300))

    def redraw(self):
        pygame.display.flip()
