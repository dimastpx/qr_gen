import qrcode
import telebot
from PIL import Image
from os import remove

token = "7103218621:AAG0OMIpTCQVir27XZDIclrqIS5my0rv0LI"
bot = telebot.TeleBot(token)


def savelink(link : str):

    qr = qrcode.make(link)
    path = "code.png"
    qr.save(path)
    file = Image.open(path)
    return file


@bot.message_handler(content_types=["text"])
def send(message):
    bot.send_photo(chat_id=message.chat.id, photo=savelink(message.text))
    remove("code.png")

bot.polling()