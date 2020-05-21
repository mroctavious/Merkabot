import telebot

##This function will read configuration file and set the options for the program to work
#config options can be defined by the user during runtime
def readConfigFile(configFilename):
    config = {}
    with open(configFilename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith("#") or "=" not in line:
                continue
            data=line.split("=")
            option=data[0].strip()
            value=data[1].strip()
            config[option]=value
    return config
#https://github.com/eternnoir/pyTelegramBotAPI

config=readConfigFile("Merkabot.cfg")

##Starting the bot
bot = telebot.TeleBot(config['BOT_TOKEN'])


@bot.message_handler(commands=['start', 'help'])
def pko(message):
    bot.reply_to(message, "Hola Pi pi pi Pita")

#/ubi
@bot.message_handler(commands=['ubi'])
def ubica(message):
    bot.send_location(message.chat.id, 20.618217, -100.397134)

# sendLocation
#20.618217, -100.397134
#tb.send_location(chat_id, lat, lon) 

    


##Ejecutar el bot
bot.polling()

# sendMessage
#tb.send_message(chat_id, text)   ##DOMINADO


# All send_xyz functions which can take a file as an argument, can also take a file_id instead of a file.
# sendPhoto
#
#tb.send_photo(chat_id, photo)  ##DOMINADO
#tb.send_photo(chat_id, "FILEID")

#/ubi
# sendLocation
#20.618217, -100.397134
#tb.send_location(chat_id, lat, lon) 
