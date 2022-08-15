import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "+", selfbot = True)

account_token = 'Discord account token'
application_id = 972841533600567356
large_image_id = '1008393123933724752'


@bot.event
async def on_ready():
	await bot.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			details = "мышь крутиться (дрифтит) под клевый фонк",
			name = "мышь крутиться (дрифтит) под клевый фонк",
			assets = {
			  'large_image' : large_image_id,
			  'large_text':'t.me/player24x7'
			},
			url = "https://www.twitch.tv/artem_bay1"
			)
		)
	print('Успешный запуск!')

bot.run(account_token, bot = False)