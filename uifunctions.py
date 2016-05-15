#!/usr/bin/python2.7
# -*- coding: utf8 -*

import pygame

def imgLoader(path):
    imgObject = pygame.image.load(path).convert_alpha()
    return imgObject
