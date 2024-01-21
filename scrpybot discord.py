import discord
import pyautogui
from discord.ext import tasks, commands

TOKEN = 'MTE5MjIyNjQwOTE4NDIzNTUzMA.Glh4tV.l0nJuKQQ5MSKlNPRYGsfV3jwNBKhBfK2JICxVQ'
CHANNEL_ID = 1192218503692959747  # Replace with your channel ID

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(seconds=1)  # Adjust the time interval as needed
async def send_screenshot():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')

        with open('screenshot.png', 'rb') as file:
            screenshot_file = discord.File(file)
            await channel.send(file=screenshot_file)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_screenshot.start()

bot.run(TOKEN)
