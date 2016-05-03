#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame


class UI(object):
    """UI Class, handles all UI related stuff"""
    def __init__(self, arg):
        super(UI, self).__init__()
        self.arg = arg
        pygame.init()

    def createMainWindow(self):
        # create game window
        self.window = pygame.display.set_mode((640, 480))

        # create background and stick it on the window
        self.background = pygame.image.load("assets/img/background.png")
        self.background = self.background.convert()

        self.window.blit(self.background, (0, 0))

        self.isAlive = True

    def handleEvent(self, pet):
        """define action to be taken depending on user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isAlive = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pet.feed()

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
