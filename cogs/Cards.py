# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:51:53 2022

@author: Tristen
"""
import discord
from discord.ext import commands
from random import randrange,choice,shuffle
import pdb

import games

class Cards(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def draw(self, ctx, n=1): #Draws n cards and adds them to a player's hand
        
       # pdb.set_trace()
        hand=games.Hand(ctx.author)
        deck=games.Deck()
        
        
        
        for i in range(n):
            hand.cards.append(deck.draw())
        await ctx.reply(hand)

            
  
def setup(bot):
    bot.add_cog(Cards(bot))
    
            