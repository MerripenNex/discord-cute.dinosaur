# Importing necessary libraries. Discord.py is important to interact with the Discord API and numpy for manipulating the arrays, whereas random is needed for a random process.
import discord, numpy, random
from discord.ext import commands

# Defining the start-up conditions and setting the Intents.
client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
intents = discord.Intents.default()
intents.members = True
prefix = '!'

# Defining a class needed for the sorting hat process.
class House:
    houses = [ [], [], [], [] ]
    housenames = {'Cepheus' : houses[0], 'Eta' : houses[1], 'Polaris' : houses[2], 'Aquilia' : houses[3]}

# Defining a class to interact with the Discord API & Client.
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == self.user:
            return

        if message.content.startswith(prefix + 'help'):
            await message.channel.send(prefix + 'help')

        if message.content.startswith(prefix + 'myHouse'):
            # Getting the user's ID, querying a random number and assigning the user's ID to the house
            d_userid = message.author.id
            randomHouse = random.randint(0,3)
            House.houses[randomHouse].append(d_userid)

            # Getting the name of the house and sending a message as output.
            def get_key(val):
                for key, value in House.housenames.items():
                    if val == value:
                        return key

           user_house = get_key(House.houses[randomHouse])
           await message.channel.send('Your house is ' + str(user_house) + '!')


