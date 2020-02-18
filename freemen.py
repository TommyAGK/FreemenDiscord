import os
import random
import asyncio

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)



class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None 


    @commands.Cog.listener()
    async def someevent(self, e):
        await None


        
    @commands.command()
    async def myRoles(self, context, *, member: discord.member = None):
        """ responds with your roles """
        member = member or context.author
        if self._last_member is None or self._last_member.id != member.id:
            jobs = list()
            
            for role in member.roles:
                print(role)
                if "everyone" in role.name:
                    continue
                else:
                    jobs.append(role.name)
            roles = ", ".join(jobs)
            await context.send(f"Yes? oh, you're a member of : {roles}")
        else:
            await context.send(f"I just told you tho, didnt i {member}?")
        self._last_member = member

    @commands.Cog.listener()
    async def on_reaction_add(reaction, user):
        print("saw reaction")
        if str(reaction.emojii) == ":ok_hand:":
            await reaction.message.channel.send(":ok_hand:")




class Utility(commands.Cog):
    @bot.event
    async def on_message(message):
        if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')

        else:
            await channel.send('👍')







print("starting bot")
bot.add_cog(RoleManagement(bot))
bot.add_cog(Utility(bot))
bot.run(token)


