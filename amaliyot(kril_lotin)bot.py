from translate import to_cyrillic, to_latin
import telebot
TOKEN = '7143828073:AAGRzdSlnuQXAZgT0B5sycbLVXy-s49UEt8'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    javob = "Assalomu alaykum , Xush kelibsiz"
    javob += "\nMatn kiriting:"
    bot.reply_to(message,javob)



@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
bot.polling()

"""matn = input("Matn kiriting: ")


else:
  print()
#7143828073:AAGRzdSlnuQXAZgT0B5sycbLVXy-s49UEt8"""