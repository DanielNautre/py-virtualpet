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
        pass
