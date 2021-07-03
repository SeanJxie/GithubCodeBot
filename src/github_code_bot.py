import re
import os

import discord
import aiohttp
import asyncio

#print(f"Discord: {discord.__version__} aiohttp: {aiohttp.__version__}")

# Handle bot token input
BT_FILEPATH = os.path.join(os.getcwd(), "bot_token.txt")
if os.path.exists(BT_FILEPATH):
    with open(BT_FILEPATH, 'r') as btf:
        TOKEN = btf.readline()
else:
    TOKEN = input("Enter bot token here (this happens only once): ")
    with open(BT_FILEPATH, 'w') as btf:
        btf.write(TOKEN)

# Handle command character input
CC_FILEPATH = os.path.join(os.getcwd(), "cmd_char.txt")
if os.path.exists(CC_FILEPATH):
    with open(CC_FILEPATH, 'r') as ccf:
        CMD_CHAR = ccf.readline()
else:
    CMD_CHAR = input("Enter your command character here (this happens only once): ")
    while len(CMD_CHAR) != 1:
        print("The command character is ONE character only. Please retry.")
        CMD_CHAR = input("Enter your command character here (this happens only once): ")
    with open(CC_FILEPATH, 'w') as ccf:
        ccf.write(CMD_CHAR)

# For pyinstaller exe compilation
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
 
COMMON_EXTS = (
    "asm",
    "c",
    "cc",
    "class",
    "clj",
    "cpp",
    "cs",
    "cxx",
    "el",
    "go",
    "h",
    "java",
    "lua",
    "m",
    "md",
    "m4",
    "php",
    "pl",
    "po",
    "py",
    "rb",
    "rkt"
    "rs",
    "sh",
    "s",
    "swift",
    "vb",
    "vcxproj",
    "xcodeproj",
    "xml",
    "diff",
    "patch",
    "html",
    "js",
    "json",
    "csv",
)

PAYLOAD_MAXLEN = 2000 # Discord character limit
HEX_YELLOW = 0xFFDF00
HEX_LBLUE  = 0xADD8E6

# Some helpful functions
def get_ext(urlStr):
    return urlStr[urlStr.rfind('.') + 1:].lower()


class BotClient(discord.Client):
    long_code = True
    paused = False
    aiohttp_session = None

    async def init_session():
        BotClient.aiohttp_session = aiohttp.ClientSession()

    async def on_ready(self):
        print(f"{self.user} is now online.")
        self.user.name = "GithubCodeBot"
        print("Username set.")

        with open(resource_path("src/octo.png"), "rb") as pfp:
            try:
                await self.user.edit(avatar=pfp.read())
                print("Avatar set.")
            except discord.errors.HTTPException:
                # In the case that the bot is started many times, Discord may complain that we're setting pfp too much. 
                pass 
        
        await BotClient.init_session()
        print("Ready.")    
        
    async def on_message(self, msg):
        if msg.author == self.user:
            return 

        elif msg.content.startswith(f"{CMD_CHAR}longcode"):
            if not BotClient.long_code:
                await msg.channel.send(f"> :green_circle: Alright! I'll display code over the {PAYLOAD_MAXLEN} character limit!")
                BotClient.long_code = True

            else:
                await msg.channel.send(f"> :red_circle: Alright! I'll only display code under the {PAYLOAD_MAXLEN} character limit!")
                BotClient.long_code = False

        elif msg.content.startswith(f"{CMD_CHAR}pause"):
            if not BotClient.paused:
                await msg.channel.send(f"> :pause_button: No problem! I'll stay quiet until you type `{CMD_CHAR}pause` again.")
                BotClient.paused = True

        elif msg.content.startswith(f"{CMD_CHAR}unpause"):
            if BotClient.paused:
                await msg.channel.send(f"> :arrow_forward: I'm back! Type `{CMD_CHAR}pause` if you want me to stay quiet again.")
                BotClient.paused = False

        elif msg.content.startswith(f"{CMD_CHAR}status"):
            embed = discord.Embed(title="GithubCodeBot :robot: Status:", color=HEX_YELLOW)
            embed.add_field(name="Paused", value=f">>> `{BotClient.paused}`", inline=False)
            embed.add_field(name="Preview long code", value=f">>> `{BotClient.long_code}`", inline=False)
            await msg.channel.send(embed=embed)

        elif msg.content.startswith(f"{CMD_CHAR}help"):
            embed = discord.Embed(title="GithubCodeBot :robot: Commands", description="_Here's what you can ask me to do!_", color=HEX_LBLUE)
            embed.add_field(name=f"`{CMD_CHAR}pause`", value=">>> I wont respond to any Github links. I'll still be actively listening for commands, though!", inline=False)
            embed.add_field(name=f"`{CMD_CHAR}unpause`", value=">>> Whatever `pause` does, this un-does.", inline=False)
            embed.add_field(name=f"`{CMD_CHAR}longcode`", value=">>> Toggle my ability to preview long pieces of code (by splitting the code into multiple messages). Be carefull with this! Once I get going, I won't stop!", inline=False)
            embed.add_field(name=f"`{CMD_CHAR}status`", value=">>> View my `pause` and `longcode` states.", inline=False)
            embed.add_field(name=f"`{CMD_CHAR}help`", value=">>> You're looking at it!", inline=False)
           
            await msg.channel.send(embed=embed)


        elif not BotClient.paused:
            # The strange process looks like this:
            #
            # (1) https://github.com/SeanJxie/3d-engine-from-scratch/blob/main/CppEngine3D/engine.cpp
            #                                            |
            #                                            V
            # (2) ['https:', '', 'github.com', 'SeanJxie', '3d-engine-from-scratch', 'blob', 'main', 'CppEngine3D', 'engine.cpp']
            #                                            |
            #                                            V
            # (3) ['https:/', 'raw.githubusercontent.com', 'SeanJxie', '3d-engine-from-scratch', 'main', 'CppEngine3D', 'engine.cpp']
            #                                            |
            #                                            V
            # (4) https://raw.githubusercontent.com/SeanJxie/3d-engine-from-scratch/main/CppEngine3D/engine.cpp

            print(f"\nMessage: {msg.content}")
            matches = re.findall("http(s?)://(www\.)?github.com/([^\s]+)", msg.content)

            # We want no reps and valid extensions.
            matches = list(dict.fromkeys(filter(lambda x: get_ext(x[-1]) in COMMON_EXTS, matches)))

            if len(matches) > 1:
                await msg.channel.send(f"> :eyes: I've detected {len(matches)} valid links here. They will be served in order!")

            if len(matches) != 0:
                for match in matches:

                    # (1)
                    url = "https://github.com/" + match[-1]
                    print(f"\nDetected url: {url}")

                    # (2)
                    urlSplit = url.split('/')
                    
                    # (3)
                    urlSplit.remove('')
                    if "blob" in urlSplit:
                        urlSplit.remove("blob")
                    elif "tree" in urlSplit:
                        urlSplit.remove("tree")

                    urlSplit[0] = "https:/"
                    urlSplit[1] = "raw.githubusercontent.com"

                    # (4)
                    rawUrl = '/'.join(urlSplit)
                    print(f"Rebuilt url: {rawUrl}")

                    # Parse HTML and get all text
                    async with BotClient.aiohttp_session.get(rawUrl) as response:
                        codeString = await response.text()
                    payload = f"```{codeString}```"
                    
                    if len(payload) <= PAYLOAD_MAXLEN:
                        await msg.channel.send(f"> :desktop: The following code is found in `{urlSplit[-1]}`:")
                        await msg.channel.send(payload)

                    # Send text and split into multiple messages if it's too long
                    elif BotClient.long_code:
                        await msg.channel.send(f"> :desktop: The following code is found in `{urlSplit[-1]}`:")
                        print("Code too long. Splitting.")

                        payloadSegment = ''

                        for line in codeString.split('\n'):
            
                            if len(payloadSegment) + len(line) + 6 >= PAYLOAD_MAXLEN: # The +6 accounts for the 6 backticks used for code markup
                                await msg.channel.send(f"```{payloadSegment}```")
                                print(f"Payload segment size: {len(payloadSegment) + 6}")
                                payloadSegment = ''

                            payloadSegment += line + '\n'

                        await msg.channel.send(f"```{payloadSegment}```")
                        print(f"Payload segment size: {len(payloadSegment) + 6}")

                    else:
                        await msg.channel.send(f"> That's a lot of code! Type `!long_code` to toggle my long code reading ability!")

                    await msg.channel.send(f"> :ok_hand: That's the end of `{urlSplit[-1]}`")
                    print("Send success.")



def main():
    print("\nThanks for using GithubCodeBot!\nIf you'd like to reset your bot token or command character, simply delete bot_token.txt or cmd_char.txt and reset the program.\n\nConnecting...\n")

    bot_client = BotClient()
    try:
        bot_client.run(TOKEN)
    except discord.errors.LoginFailure:
        os.remove(BT_FILEPATH)
        print("The token you've entered is invalid. Please restart the program.")


if __name__ == "__main__":
    main()