from datetime import datetime

class XXXXXXXController:
    def __init__(self):
        None
    
    def start(self, bot, update):
        chat = update.message.chat
        update.message.reply_text('Mensaje de entrada')

    def help(self, bot, update):
        chat = update.message.chat
        update.message.reply_text('Mensaje de ayuda')
	
    def processText(self, bot, update):
        chat = update.message.chat
        username = chat.username
        message = update.message.text
        print(message)
        # echo texto
        update.message.reply_text('{0} escribe: {1}'.format(username, message))

    def processImage(self, bot, update):
        chat = update.message.chat
        username = chat.username
        tiempo = str(datetime.now())
        archivo = '{0}_{1}.jpg'.format(tiempo, username)
        image_input = archivo
        print(image_input)

        file = bot.getFile(update.message.photo[-1].file_id)
        file.download(image_input)

        # echo imagen
        bot.send_photo(chat_id = chat.id, photo = open(image_input, 'rb'))
    
    def buttonsController(self, bot, update):
        None
