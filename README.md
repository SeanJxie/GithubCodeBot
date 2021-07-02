# DiscordCodeBot
A discord bot that searches for valid Github code links and displays them with `bs4` and the `discord` api.
![example](https://github.com/SeanJxie/DiscordCodeBot/blob/main/example.jpg)
Why didn't I use the Github API? I don't know. It's a good web-scraping exercise, though.

# Commands
Just one: `!longcode` toggles the bot's ability to display code over the 2000 character limit on Discord.

# Setup
- Follow the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html) to obtain a bot token. 
- Paste the token in the `bot_token` file. 
- Invite the bot to your server. The instructions to invite the bot can also be found in the previous link. The bot should have `Send Messages` and `Read Message History` permissions only.
- Run the Python script with the appropriate packages (`bs4`, `discord`) installed.
