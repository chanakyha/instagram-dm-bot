from instabot import Bot
import json

credentials = json.load(open('credentials.json'))


bot = Bot()

# Login to Instagram
bot.login(username=credentials["username"], password=credentials["password"])