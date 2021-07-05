# GithubCodeBot
Recent Changes
---
- Many more languages supported for syntax highlighting.
- Backticks in code can now be displayed properly.
- Syntax highlighting has been added thanks to Discord's `highlight.js` integration.
- Now using `discord.ext.commands.Bot` instead of `discord.Client`.
- Now using `aiohttp` for webscraping instead of `requests`.

![demo](https://github.com/SeanJxie/DiscordCodeBot/blob/main/bot_demo.gif)

# EXE Setup
1) Follow the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html#creating-a-bot-account) to create a bot and obtain a bot token (you don't need to worry about the application/bot name or avatar). **Save the bot token for later.**
---
2) Download and run [`GithubCodeBot.exe`](https://github.com/SeanJxie/DiscordCodeBot/blob/main/GithubCodeBot.exe?raw=true).
You will be prompted for your bot token and command prefix. 
---
3) Follow the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot) to invite the bot to a server of your choice. **The bot should have the `Send Messages`permission only.**
---

# Python Windows Setup
Requirements: [`python 3.5` or higher](https://www.python.org/downloads/), [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), and [`pip`](https://pip.pypa.io/en/stable/installing/).
1) Follow the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html#creating-a-bot-account) to create a bot and obtain a bot token (you don't need to worry about the bot name or avatar). **Save the bot token for later.**
---
3. **If the requirements are fulfilled, in a target directory, clone the repo:**
```
git clone https://github.com/SeanJxie/GithubCodeBot
```
---
4. **Next, move into the repo:**
```
cd GithubCodeBot
```
---
5. **Then, install the required packages:**
```
py -m pip install -r requirements.txt
```
---
6. **Move into the `src` folder and run the bot:**

```
cd src
py github_code_bot.py
```
You will be prompted for your bot token and command prefix.
---
7) Follow the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot) to invite the bot to a server of your choice. **The bot should have the `Send Messages`permission only.** After this you should be good to go!
---
# Commands
The bot's `help` command outlines it all.

