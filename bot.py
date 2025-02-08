from dotenv import load_dotenv,dotenv_values
load_dotenv()
import discord
import os
from discord.ext import commands
from discord import app_commands
intents = discord.Intents.default()
intents.message_content = True

class Client(commands.Bot):  # Renamed to avoid confusion
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        try:
            GUILD = discord.Object(id=953255670327693312)
            synced= await self.tree.sync(guild=GUILD)
            print(f"synced {len(synced)} commmand to guild {GUILD.id}")
        except Exception as e:
            print(f"error syncing command {e}")


### dekh ye on_message wala jo hai naa function uska use karke bahoot kuch automate kar skte hai koi help likhega to ye wala trigger ho jayega wagera 
   ## ye on_ready ya on_message ye naming hi use karna hai specific function hai kuch bhi nahi rakh skte  hai 
    async def on_message(self,msg):
        if msg.author==self.user:
            return
        if msg.content.startswith('hello'):
            await msg.channel.send(f"hi there {msg.author}")
    # this is for adding message when user reacted to some message is ko haam like ( usr ko kuch denge option agar user ne rye react kiya to ye wala taks perform karo kuch aur react kiya to kuch aur karo wagera idea likh raha hu bas age dekh lena )
    async def on_reaction_add(self,reaction,user):
        await reaction.message.channel.send(f"you reacted {user.name,reaction.emoji} ")
# Use the custom class MyClient instead of the base discord.Client
client=Client(command_prefix="!",intents=intents)
# ye wala command banane ke liye 
#953255670327693312
GUILD_ID = discord.Object(id=953255670327693312)
@client.tree.command(name="hello",description="say hello!",guild=GUILD_ID)
async def sayHello(interaction:discord.Interaction):
    await interaction.response.send_message("hi there!")
@client.tree.command(name="printer",description="sprint ",guild=GUILD_ID)
async def printer(interaction:discord.Interaction,printer: str):
    await interaction.response.send_message(f"printing hat u want {printer}")
@client.tree.command(name="help",description="details",guild=GUILD_ID)
async def sayHello(interaction:discord.Interaction):
    embed= discord.Embed(title="Commands",url="https://www.youtube.com/watch?v=KHQ2MaDbx5I&t=342s",description="commands details",color=discord.Color.red())
    await interaction.response.send_message(embed=embed)

class View(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.red, emoji="🔥")
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you clicker the button")
@client.tree.command(name="button",description="display button ",guild=GUILD_ID)
async def mybutton(interaction:discord.Interaction):
    await interaction.response.send_message(view=View())
client.run(os.getenv("Token"))
