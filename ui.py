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
        self.window = pygame.display.set_mode((640, 480))
        self.isAlive = True
        pass

    def handleEvent(self, pet):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isAlive = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pet.feed()
