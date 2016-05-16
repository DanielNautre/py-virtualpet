#!/usr/bin/python2.7
# -*- coding: utf8 -*

from collections import defaultdict

moodlets = defaultdict(dict)

# name: Title of the moodlet
# desc: description of the moodlet
# stackable: does it stack and to which max value
# value: which effect on the mood does the moodlet have
# duration: how long does the moodlet last (-1 = forever)

moodlets['fed']['name'] = "Well Fed"
moodlets['fed']['desc'] = "Your pet just had a good meal"
moodlets['fed']['stackable'] = False
moodlets['fed']['value'] = 15
moodlets['fed']['duration'] = 60

moodlets['dirty']['name'] = "Dirty"
moodlets['dirty']['desc'] = "Your pet is dirty, you should clean it"
moodlets['dirty']['stackable'] = False
moodlets['dirty']['value'] = -15
moodlets['dirty']['duration'] = -1

moodlets['pet']['name'] = "pet"
moodlets['pet']['desc'] = ""
moodlets['pet']['stackable'] = 30
moodlets['pet']['value'] = 5
moodlets['pet']['duration'] = 30

moodlets['hungry']['name'] = "Hungry"
moodlets['hungry']['desc'] = "Your pet is hungry, you should feed it"
moodlets['hungry']['stackable'] = False
moodlets['hungry']['value'] = -10
moodlets['hungry']['duration'] = -1

moodlets['starve']['name'] = "Starving"
moodlets['starve']['desc'] = "Your pet is starving, you should feed it"
moodlets['starve']['stackable'] = False
moodlets['starve']['value'] = -30
moodlets['starve']['duration'] = -1

moodlets['clean']['name'] = "Clean"
moodlets['clean']['desc'] = "Your pet is clean and feels good"
moodlets['clean']['stackable'] = False
moodlets['clean']['value'] = 15
moodlets['clean']['duration'] = -1

moodlets['sad']['name'] = "Sad"
moodlets['sad']['desc'] = "Your pet feels sad for no good reason, it'll pass"
moodlets['sad']['stackable'] = False
moodlets['sad']['value'] = -10
moodlets['sad']['duration'] = 90
