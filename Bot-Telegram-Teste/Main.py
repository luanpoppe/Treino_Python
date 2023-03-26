import telebot

chave_api = "6018909502:AAFIeJ17s0AbyqwiakoBS21l42UnUGahc3w"

bot = telebot.TeleBot(chave_api)



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    var_texto = "asasasdasda"
    bot.reply_to(mensagem, var_texto)

bot.polling()