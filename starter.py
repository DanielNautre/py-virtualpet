#!/usr/bin/python2.7
# -*- coding: utf8 -*

import Tkinter


class starter(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("300x200")
        self.run()

    def run(self):
        self.nameField = Tkinter.Entry()
        self.nameField.focus_set()
        self.nameField.pack()
        createBtn = Tkinter.Button(self, text="Create", command=self.createPet)
        createBtn.pack()
        self.bind("<return>", self.createPet)

    def createPet(self):
        self.name = self.nameField.get()
        self.destroy()
