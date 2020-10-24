import discord
import csv
from discord.ext import commands

client = commands.Bot(command_prefix="!")

queueList = []

@client.event
async def on_ready():
    print("Queue bot ready")

#Command for adding oneself to the queue
@client.command()
async def add(ctx):
    if ctx.author.id in queueList:
        await ctx.send("You're already in the queue")
    else:
        queueList.append(ctx.author.id)
        await ctx.send(ctx.author.name + " has been added to the queue in position " + str(len(queueList)))

#Command for clearing the entire queue
@client.command()
async def clear(ctx):
    queueList.clear()
    await ctx.send("Queue has been cleared")

#Command for showing the entire queue
@client.command()
async def queue(ctx):
    listLength = len(queueList)
    if listLength == 0:
        await ctx.send("Queue is empty")
    else:
        queueString = "The people in the queue are "
        for x in range(listLength):
            user = client.get_user(int(queueList[x]))
            username = user.name
            queueString += str(username)

            #Adds a "," if it's not the last user in the queue
            if x+1 != listLength:
                queueString += ", "

        await ctx.send(queueString)

#Command for removing oneself from the queue
@client.command
async def leave(ctx):
    if ctx.author.id in queueList:
        queueList.remove(ctx.author.id)
    else:
        await ctx.send("You're not in the queue")

#Command for removing based on username username
@client.command
async def remove(ctx, user):
    try:
        person = discord.utils.get(message.guild.members, name=user)
        queueList.remove(member.id)
        await ctx.send("Succesfully removed " + person.name + " from the queue")
    except:
        await ctx.send("Error in removing person. Worst case, use !clear and have people rejoin")

#Command for allowing the next person to join.
@client.command()
async def next(ctx, number=1):
    for x in range(number):
        if len(queueList) != 0:

            id = '<@' + str(queueList[0]) + '>'
            del queueList[0]
            user = ctx.guild.get_member(id)

            await ctx.send('%s' ", you're up next"% id)
        else:
            await ctx.send("Queue is empty")
            if x!=number and number-x != 1 :
                await ctx.send("There are " + str(number-x)  + " empty spots")

            elif x!=number and number-x == 1 :
                await ctx.send("There is " + str(number-x)  + " empty spot")
            break

client.run("")
