#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame
import uisettings as uis
import strings as s

from uifunctions import imgLoader


class UI(object):
    """UI Class, handles all UI related stuff"""

    def __init__(self, arg):
        super(UI, self).__init__()
        self.arg = arg
        pygame.init()

    def loadImages(self):
        """Load images into memory"""

        # Load the background
        self.background = imgLoader(uis.backgroundDayImgPath)
        self.gaugeEmptyImg = imgLoader(uis.gaugeEmptyImgPath)
        self.gaugeFullImg = imgLoader(uis.gaugeFullImgPath)

        # Load Pet images
        self.aliveImg = imgLoader(uis.aliveImgPath)
        self.deadImg = imgLoader(uis.deadImgPath)

        # Load UI elements
        self.feedBtnImg = imgLoader(uis.feedBtnPath)
        self.healBtnImg = imgLoader(uis.healBtnPath)
        self.idCardImg = imgLoader(uis.idCardPath)

        # Load Moodlets images
        self.moodletImg = {}
        self.moodletImg["fed"] = imgLoader(uis.fedImgPath)
        self.moodletImg["dirty"] = imgLoader(uis.fedImgPath)

    def createMainWindow(self):
        # create game window
        pygame.display.set_caption(s.windowLbl)
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

                mousePos = pygame.mouse.get_pos()

                # Feed ?
                if self.feedBtn.collidepoint(mousePos):
                    pet.feed()
                    continue

                # Heal ?
                if self.healBtn.collidepoint(mousePos):
                    pet.heal()
                    continue

    def drawBackground(self):
        self.window.blit(self.background, (0, 0))

    def drawUserInterface(self, pet):
        self.feedBtn = self.window.blit(self.feedBtnImg, uis.feedBtnPos)
        self.healBtn = self.window.blit(self.healBtnImg, uis.healBtnPos)       

        self.drawIdCard(pet)
        self.drawHappinessGauge(pet)

    def drawIdCard(self, pet):
        self.window.blit(self.idCardImg, uis.idCardPos)
        font = pygame.font.Font(None, 18)
        self.nameLbl = font.render(pet.name, 1, (0, 0, 0))
        self.window.blit(self.nameLbl, (130, 465))

    def drawHappinessGauge(self, pet):
        self.window.blit(self.gaugeEmptyImg, uis.gaugeEmptyPos)
        crop = (0, 0, pet.getCurrentMood() * 2, 50)
        self.window.blit(self.gaugeFullImg, uis.gaugeFullPos, crop)

    def drawMoodlets(self, pet):
        i = 0
        for mood in pet.activeMood.iteritems():
            posX = uis.WINSIZE[0] - (uis.moodletSpacer[0] + uis.moodletSize[0])
            posY = uis.moodletSpacer[1] + (i * (uis.moodletSpacer[0] + uis.moodletSize[0]))
            self.window.blit(self.moodletImg[mood[0]], (posX, posY))
            i = i + 1

    def drawPet(self, pet):
        if pet.alive is True:
            self.window.blit(self.aliveImg, (250, 300))
        else:
            self.window.blit(self.deadImg, (250, 300))

    def redraw(self, pet):
        self.drawBackground()
        self.drawPet(pet)
        self.drawUserInterface(pet)
        self.drawMoodlets(pet)

        pygame.display.flip()

    def setTickSpeed(self, value):
        pygame.time.Clock().tick(value)
