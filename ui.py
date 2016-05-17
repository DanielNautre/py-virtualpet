#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame
import uisettings as us
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
        self.background = imgLoader(us.backgroundDayImgPath)

        # Load Pet images
        self.aliveImg = imgLoader(us.aliveImgPath)
        self.deadImg = imgLoader(us.deadImgPath)

        # Load UI elements
        self.feedBtnImg = imgLoader(us.feedBtnPath)
        self.healBtnImg = imgLoader(us.healBtnPath)
        self.cleanBtnImg = imgLoader(us.cleanBtnPath)
        self.idCardImg = imgLoader(us.idCardPath)
        self.gaugeEmptyImg = imgLoader(us.gaugeEmptyImgPath)
        self.gaugeFullImg = imgLoader(us.gaugeFullImgPath)

        # Load Moodlets images
        self.moodletImg = {}
        self.moodletIco = {}
        self.moodletImg["fed"] = imgLoader(us.fedImgPath)
        self.moodletImg["dirty"] = imgLoader(us.dirtyImgPath)

    def createMainWindow(self):
        # create game window
        pygame.display.set_caption(s.windowLbl)
        self.window = pygame.display.set_mode(us.WINSIZE)

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
        """displays tooltip depending on mouse position"""
        mousePos = pygame.mouse.get_pos()

        # check if mouse hover a moodlet icon
        for mood in self.moodletIco:
            if self.moodletIco[mood].collidepoint(mousePos):
                title = m.moodlets[mood]["name"]
                text = m.moodlets[mood]["desc"].split("\n")
                print text
                self.drawTooltip(mousePos, title, text)

        if self.feedBtn.collidepoint(mousePos):
            self.drawTooltip(mousePos, "Feed your pet")

        if self.healBtn.collidepoint(mousePos):
            self.drawTooltip(mousePos, "Heal your hurt pet")

        if self.cleanBtn.collidepoint(mousePos):
            self.drawTooltip(mousePos, "clean the your pet")

    def drawUserInterface(self, pet):
        """draws all the UI elements"""
        self.feedBtn = self.window.blit(self.feedBtnImg, us.feedBtnPos)
        self.healBtn = self.window.blit(self.healBtnImg, us.healBtnPos)
        self.cleanBtn = self.window.blit(self.cleanBtnImg, us.cleanBtnPos)

        self.drawIdCard(pet)
        self.drawHappinessGauge(pet)

    def drawIdCard(self, pet):
        self.window.blit(self.idCardImg, us.idCardPos)
        font = pygame.font.Font(None, 22)
        self.nameLbl = font.render(pet.name, 1, (0, 0, 0))
        self.window.blit(self.nameLbl, (130, 465))

    def drawHappinessGauge(self, pet):
        """Draw top gauge to indicate hapiness level"""
        self.window.blit(self.gaugeEmptyImg, us.gaugeEmptyPos)
        crop = (0, 0, pet.getCurrentMood() * 2, 50)
        self.window.blit(self.gaugeFullImg, us.gaugeFullPos, crop)

    def drawMoodlets(self, pet):
        i = 0
        for mood in pet.activeMood.iteritems():
            posX = us.WINSIZE[0] - (us.moodletSpacer[0] + us.moodletSize[0])
            posY = us.moodletSpacer[1] + (i * (us.moodletSpacer[0] + us.moodletSize[0]))
            self.moodletIco[mood[0]] = self.window.blit(self.moodletImg[mood[0]], (posX, posY))
            i = i + 1

    def drawPet(self, pet):
        if pet.alive is True:
            self.window.blit(self.aliveImg, (250, 300))
        else:
            self.window.blit(self.deadImg, (250, 300))

    def redraw(self, pet):
        """Handle drawing of the game window"""
        self.window.blit(self.background, (0, 0))

        self.drawPet(pet)
        self.drawUserInterface(pet)
        self.drawMoodlets(pet)

        # handle tooltips
        self.handleToolTips(pet)

        pygame.display.flip()

    def setTickSpeed(self, value):
        pygame.time.Clock().tick(value)

    def drawTooltip(self, pos, title, text=""):
        # calculate size of the TT
        margins = 15
        titleFontSize = 18
        textFontSize = 14

        width = (margins * 2) + 170
        height = (margins * 3) + titleFontSize + (textFontSize * len(text))

        # Calculate starting position for the TT
        startX = pos[0]
        startY = pos[1]

        if width + pos[0] > us.WINSIZE[0]:
            startX = pos[0] - width
        if height + pos[1] > us.WINSIZE[1]:
            startY = pos[1] - height

        rect = (startX, startY, width, height)
        outline = (startX + 5, startY + 5, width - 10, height - 10)

        # draw the TT
        pygame.draw.rect(self.window, us.TTBCK, rect, 0)
        pygame.draw.rect(self.window, us.TTOUTLINE, outline, 1)

        titleFont = pygame.font.Font(None, titleFontSize)
        textFont = pygame.font.Font(None, textFontSize)

        titleLbl = titleFont.render(title, 1, us.TTTEXT)
        self.window.blit(titleLbl, (startX + margins, startY + margins))

        i = 0
        for line in text:
            posY = startY + titleFontSize + (2 * margins) + (i * textFontSize)
            textLbl = textFont.render(line, 1, us.TTTEXT)
            self.window.blit(textLbl, (startX + margins, posY))
            i = i + 1
