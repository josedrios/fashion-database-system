"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
import os
from discord.ext import commands
from models import TestModel, Employer
from database import Database

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command(name="test", description="write your database business requirement for this command here")
async def _test(ctx, arg1):
    testModel = TestModel(ctx, arg1)
    response = testModel.response()
    await ctx.send(response)


@bot.event 
async def on_ready(): 
    print(f"Bot {bot.user} has joined the room") # the bot is online
    Database.connect(bot.user) # bot is connected to the database

# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.

# EMPLOYER NAME
@bot.command(name="find_name", description="This will find an employer")
async def find_employer(ctx, employer_id):
  employer = Employer.get(employer_id)
  name = employer._name 
  await ctx.send(name)

# EMPLOYER GENDER
@bot.command(name="find_gender", description="This will find an employer's gender")
async def find_gender(ctx, employer_id):
  employer = Employer.get(employer_id)
  gender = employer._gender
  await ctx.send(gender)

# EMPLOYER BIOGRAPHY
@bot.command(name="find_biography", description="This will find an employer's biography")
async def find_biography(ctx, employer_id):
  employer = Employer.get(employer_id)
  biography = employer._biography
  await ctx.send(biography)

# EMPLOYER TEAM ID
@bot.command(name="find_teamid", description="This will find an employer's team id")
async def find_teamid(ctx, employer_id):
  employer = Employer.get(employer_id)
  teamid = employer._team
  await ctx.send(teamid)

@bot.command(name="add_employer", description="this will add an employer")
async def _command20(ctx, employer_id, name, gender, biography, account, team, region, language, fashiongenre):
      Employer.add(employer_id, name, gender, biography, account, team, region, language, fashiongenre)
      await ctx.send("Employer added successfully")

@bot.command(name="update_employer", description="this will update an employers name")
async def _command20(ctx, employer_id, name):
      Employer.update(employer_id, name)
      await ctx.send("Employer updated successfully")

@bot.command(name="cmd7", description="database business requirement #7 here")
async def _command7(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd8", description="database business requirement #8 here")
async def _command8(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd9", description="database business requirement #9 here")
async def _command9(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd10", description="database business requirement #10 here")
async def _command10(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd11", description="database business requirement #11 here")
async def _command11(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd12", description="database business requirement #12 here")
async def _command12(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd13", description="database business requirement #13 here")
async def _command13(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd14", description="database business requirement #14 here")
async def _command14(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd15", description="database business requirement #15 here")
async def _command15(ctx, *args):
    await ctx.send("This method is not implemented yet")


bot.run(TOKEN)