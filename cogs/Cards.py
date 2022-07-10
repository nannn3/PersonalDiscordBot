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
open_hands={}

class Cards(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def draw(self, ctx, n=1): #Draws n cards and adds them to a player's hand
        
        if ctx.author not in open_hands:
           hand=games.Hand(ctx.author)
           open_hands[ctx.author]=hand
           pdb.set_trace()
        else:
           hand=open_hands.get(ctx.author)
           
        
        deck=games.Deck()
        
        
        
        for i in range(n):
            hand.add(deck.draw())
        await ctx.reply(hand)
    @commands.command()
    async def empty_hand(self,ctx):
      #  pdb.set_trace()
        if ctx.author in open_hands:
            pdb.set_trace()
            hand=open_hands.get(ctx.author)
            hand.empty()
            open_hands.pop(ctx.author,None)
            await ctx.reply("Successfully discarded your hand")
            
        else:
            await ctx.reply("You don't have a hand in play.")
    @commands.command()
    async def test_card(self,ctx):
        await ctx.reply(games.Card(randrange(1,52)))

            
  
def setup(bot):
    bot.add_cog(Cards(bot))
    
            