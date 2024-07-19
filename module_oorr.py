from pyrogram import Client, filters
import random
import time

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"`🪙{prefix_userbot}oorr`"
ccomand = " Орёл или решка."


def command_oorr(app):
    @app.on_message(filters.command("oorr", prefixes=prefix_userbot))
    def oorr_command(_, message):
        random_number = random.randint(0, 1)
        if random_number == 0:
            coin_emoji = "🌑"
            new_emoji = "**🪙 - Выпала решка!**"
        else:
            coin_emoji = "🌑"
            new_emoji = "**🦅 - Выпал орёл!**"
        sent_message = message.reply_text(coin_emoji)
        time.sleep(2)
        sent_message.edit_text(new_emoji)

print("Модуль oorr загружен!")
