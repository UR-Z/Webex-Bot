from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot
from equipment_retrieval_function import equipment_info
#from voice2text import voice2text
from dotenv import load_dotenv
import os

load_dotenv()

# Create a Bot Object
bot = WebexBot(teams_bot_token= os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"),approved_domains=["ur.com"])

#Clear default help command
bot.commands.clear()

# Add new commands for the bot to listen out for.
bot.add_command(equipment_info())

#Set new command as default
bot.help_command = equipment_info()

# Call `run` for the bot to wait for incoming messages.

bot.run()