# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:51:53 2022

@author: Tristen
"""
import discord
from discord.ext import commands
from random import randrange
class Cards(commands.Cog):
    @commands.command()
    def draw():
        return card(randrange(1,52))
#bot.add_cog(Cards(bot))

class card:
    def __init__(self,number):
        #Creates a card from a number, 1-52.
        rank=(number%13)+1 #number will be between 1 & 13, inclusive
        if rank <11 and rank != 1:
            self.rank= str(rank)
        elif rank==11:
            self.rank='Jack'
        elif rank == 12:
            self.rank='Queen'
        elif rank == 13:
            self.rank='King'
        elif rank == 1:
            self.rank='Ace'
        
        if number <14:
            self.suit="Hearts"
        elif number >= 14 and number <27:
            self.suit="Clubs"
        elif number >=27 and number <40:
            self.suit ="Diamonds"
        else:
            self.suit="Spades"
        
        
    def __repr__(self):
        return 'Card(%s of %s)' %(self.rank,self.suit)
    def __str__(self):
        suits_symbols = {'Spades':'♠','Diamonds': '♦','Hearts': '♥', 'Clubs' :'♣'}
        
        lines=[[] for i in range(9)]# create an empty list of list, each sublist is a line
        
        if self.rank== 10: #10 is the only rank we want to display 2 characters
            space=''
        else: 
            rank=self.rank[0] #Take the first part of the rank, IE, the first letter for special cards
            space=' '
        sym=suits_symbols.get(self.suit) #Grab the symbol for  the suit
        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(sym))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')
        
        result = [''.join(line) for line in lines]
        return '\n'.join(result)

    
def setup(bot):
    bot.add_cog(Cards(bot))
            