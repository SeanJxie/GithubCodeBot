import discord
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

with open("bot_token", 'r') as bt:
    TOKEN = bt.readline()

COMMON_EXTS = (
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
    "m4",
    "php",
    "pl",
    "po",
    "py",
    "rb",
    "rs",
    "sh",
    "swift",
    "vb",
    "vcxproj",
    "xcodeproj",
    "xml",
    "diff",
    "patch",
    "html",
    "js"
)

PAYLOAD_MAXLEN = 2000 # Discord character limit


class BotClient(discord.Client):
    async def on_ready(self):
        print(f"{self.user} is now online.")

    async def on_message(self, msg):
        if msg.author == self.user:
            return 
        
        else:
            if re.match(".*?http(s?)://github.com", msg.content):
                print("\nGithub link detected.")
                
                # The process looks like this:
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
                
                # (1)
                try:
                    matchSpan = re.search("http(s?)://github.com/([^\s]+)", msg.content)
                    url = msg.content[matchSpan.start(): matchSpan.end()]
                    print(f"Detected url: {url}")

                    # (2)
                    urlSplit = url.split('/')
                    if urlSplit[-1][urlSplit[-1].rfind('.') + 1:].lower() in COMMON_EXTS: # Check if extension is valid

                        # (3)
                        urlSplit.remove('')
                        urlSplit.remove("blob")
                        urlSplit[0] = "https:/"
                        urlSplit[1] = "raw.githubusercontent.com"

                        # (4)
                        rawUrl = '/'.join(urlSplit)
                        print(f"Rebuilt url: {rawUrl}")

                        # Parse HTML and get all text
                        response = urlopen(rawUrl)
                        bs4obj = BeautifulSoup(response, features="html.parser")

                        # Send text and split into multiple messages if it's too long
                        codeString = ''.join(bs4obj.find_all(text=True))
                        payload = f"```{codeString}```"
                        
                        if len(payload) <= PAYLOAD_MAXLEN:
                            await msg.channel.send(payload)

                        else:
                            await msg.channel.send(f"That's a lot of code! Give me a sec.")
                            print("Code too long. Splitting.")

                            payloadSegment = ''

                            for line in codeString.split('\n'):
                                
                                if len(payloadSegment) + len(line) + 6 > PAYLOAD_MAXLEN: # The +6 accounts for the 6 backticks used for code markup
                                    await msg.channel.send(f"```{payloadSegment}```")
                                    print(f"Payload segment size: {len(payloadSegment) + 6}")
                                    payloadSegment = ''

                                payloadSegment += line + '\n'

                            await msg.channel.send(f"```{payloadSegment}```")
                            print(f"Payload segment size: {len(payloadSegment) + 6}")

                            await msg.channel.send(f"Done!")
                            
                        print("Send success.")

                    else:
                        print("Invalid extension.")

                except (ValueError, AttributeError):
                    print("Invalid github url.")
                


if __name__ == "__main__":
    bot_client = BotClient()
    bot_client.run(TOKEN)

    
