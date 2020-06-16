import discord
from discord.ext import commands
import datetime
import descriptions
import functions

bot = commands.Bot(command_prefix='>', description="I will eat your kneecaps!")


# Commands
class KneecapsStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.KneecapHolder = 'KneecapBot'
        self.HolderMember = bot
        self.next_steal = datetime.datetime.now()

    @commands.command(brief=descriptions.holder_brief, description=descriptions.holder)
    async def holder(self, ctx):
        await ctx.send("Current kneecap owner is: **{}**".format(self.KneecapHolder))

    @commands.command(brief=descriptions.steal_brief, description=descriptions.steal)
    async def steal(self, ctx):
        if datetime.datetime.now() < self.next_steal:
            await ctx.send(
                "You need to wait {}".format(functions.chop_microseconds(self.next_steal - datetime.datetime.now())))
        elif ctx.message.author.name == self.KneecapHolder:
            await ctx.send("You are the friking holder. bruh")
        else:
            self.KneecapHolder = ctx.message.author.name
            self.next_steal = datetime.datetime.now() + datetime.timedelta(days=1)
            role = discord.utils.get(ctx.message.guild.roles, name="KneecapHolder")
            for m in role.members:
                await m.remove_roles(role)
            await ctx.send("Current kneecap owner is: **{}**".format(self.KneecapHolder))
            await ctx.message.guild.get_member_named(self.KneecapHolder).add_roles(role)

    @commands.command(brief=descriptions.give_brief, description=descriptions.give)
    async def give(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("I don't know this crackhead")
        if self.KneecapHolder != ctx.message.author.name:
            await ctx.send("You don't have the kneecaps")
        elif ctx.message.author.name == member.name:
            await ctx.send("You are the friking holder. bruh")
        else:
            self.KneecapHolder = member.name
            role = discord.utils.get(ctx.message.guild.roles, name="KneecapHolder")
            for m in role.members:
                await m.remove_roles(role)
            await ctx.send("Current kneecap owner is: **{}**".format(self.KneecapHolder))
            await ctx.message.guild.get_member_named(self.KneecapHolder).add_roles(role)

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I don\'t know this crackhead')


class OnlyForServerOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief=descriptions.setprefix_brief, description=descriptions.setprefix)
    async def setprefix(self, ctx, *, nprefix):
        if ctx.message.author != ctx.message.guild.owner:
            await ctx.send("You are not the owner bruh")
        else:
            nprefix = nprefix.strip()
            if nprefix != "":
                try:
                    prefix = nprefix
                    bot.command_prefix = prefix
                    await ctx.send("k it worked: **{}**".format(prefix))
                    await self.bot.change_presence(
                        activity=discord.Game(name="Prefix is {}".format(self.bot.command_prefix)))
                except:
                    await ctx.send("Bruh it didn't work (prefix its {})".format(self.bot.command_prefix))


class Epic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def role(self, ctx):
        try:
            if not discord.utils.get(ctx.message.guild.roles, name="KneecapHolder"):
                await ctx.message.guild.create_role(name="KneecapHolder", hoist=True, colour=discord.Colour(0x0000ff))
            role = discord.utils.get(ctx.message.guild.roles, name="KneecapHolder")
            await ctx.message.guild.get_member_named('KneecapBot').add_roles(role)
        except:
            print(ctx.message.guild.name)
            channel = discord.utils.get(ctx.message.guild.channels, name="general", type=discord.ChannelType.text)
            await channel.send(
                "@everyone Pls deti dajte mi permission aby so vedel vytvarat a spravovat roles aby sme mohli kradnut kneecaps")


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Prefix is {}".format(bot.command_prefix)))
    for server in bot.guilds:
        try:
            if not discord.utils.get(server.roles, name="KneecapHolder"):
                await server.create_role(name="KneecapHolder", hoist=True, colour=discord.Colour(0x00ffff))
            role = discord.utils.get(server.roles, name="KneecapHolder")
            await server.get_member_named('KneecapBot').add_roles(role)
        except:
            print(server.name)
            channel = discord.utils.get(server.channels, name="general", type=discord.ChannelType.text)
            await channel.send(
                "@everyone Pls deti dajte mi permission aby so vedel vytvarat a spravovat roles aby sme mohli kradnut kneecaps")

    print('READY!')


bot.add_cog(KneecapsStuff(bot))
bot.add_cog(OnlyForServerOwner(bot))
bot.add_cog(Epic(bot))
bot.run('NzIyMTgxODQ1MTcyNjE3Mjk5.XufXww.cq32036991EtTcbSPjA4RP2FM6A')
