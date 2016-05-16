#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame
import uisettings as uis
import strings as s
import moodlets as m

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

        # Load Pet images
        self.aliveImg = imgLoader(uis.aliveImgPath)
        self.deadImg = imgLoader(uis.deadImgPath)

        # Load UI elements
        self.feedBtnImg = imgLoader(uis.feedBtnPath)
        self.healBtnImg = imgLoader(uis.healBtnPath)
        self.cleanBtnImg = imgLoader(uis.cleanBtnPath)
        self.idCardImg = imgLoader(uis.idCardPath)
        self.gaugeEmptyImg = imgLoader(uis.gaugeEmptyImgPath)
        self.gaugeFullImg = imgLoader(uis.gaugeFullImgPath)

        # Load Moodlets images
        self.moodletImg = {}
        self.moodletIco = {}
        self.moodletImg["fed"] = imgLoader(uis.fedImgPath)
        self.moodletImg["dirty"] = imgLoader(uis.dirtyImgPath)

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

                # Clean ?
                if self.cleanBtn.collidepoint(mousePos):
                    pet.clean()
                    continue

    def handleToolTips(self, pet):
        mousePos = pygame.mouse.get_pos()

        # check if mouse hover a moodlet icon
        for mood in self.moodletIco:
            if self.moodletIco[mood].collidepoint(mousePos):
                self.drawTooltip(mood, mousePos, pet)

    def drawBackground(self):
        self.window.blit(self.background, (0, 0))

    def drawUserInterface(self, pet):
        self.feedBtn = self.window.blit(self.feedBtnImg, uis.feedBtnPos)
        self.healBtn = self.window.blit(self.healBtnImg, uis.healBtnPos)
        self.cleanBtn = self.window.blit(self.cleanBtnImg, uis.cleanBtnPos)

        self.drawIdCard(pet)
        self.drawHappinessGauge(pet)

    def drawIdCard(self, pet):
        self.window.blit(self.idCardImg, uis.idCardPos)
        font = pygame.font.Font(None, 22)
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
            self.moodletIco[mood[0]] = self.window.blit(self.moodletImg[mood[0]], (posX, posY))
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
        # handle tooltips
        self.handleToolTips(pet)

        pygame.display.flip()

    def setTickSpeed(self, value):
        pygame.time.Clock().tick(value)

    def drawTooltip(self, type, pos, pet):
        startX = pos[0] - 150
        startY = pos[1]
        pygame.draw.rect(self.window, uis.WHITE, (startX, startY, 150, 100), 0)

        titleFont = pygame.font.Font(None, 18)
        titleLbl = titleFont.render(m.moodlets[type]["name"], 1, (0, 0, 0))
        self.window.blit(titleLbl, (startX+10, startY+10))

        descFont = pygame.font.Font(None, 14)
        descLbl = descFont.render(m.moodlets[type]["desc"], 1, (0, 0, 0))
        self.window.blit(descLbl, (startX+10, startY+20))

