# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 2020

@author: Timothy Glew (glewt)
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = testUtility.GetNames()

#Number of curses and victory cards
nV = testUtility.GetNumVictoryCards(player_names)
nC = testUtility.GetNumCurseCards(player_names)

#Define box
box = testUtility.GetBoxes(nV)

#Initialize cost of cards in supply
supply_order = testUtility.GetSupplyOrder()

#INTRODUCTION OF BUG FOR ASSIGNMENT-2
supply_order = {0:['Curse'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Copper','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
supply = testUtility.GetSupply(box)

#The supply always has these cards
supply = testUtility.GetStandardSupply(supply, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)