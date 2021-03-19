from telegram import Update
from telegram.ext import Updater, CommandHandler
import logging
import toml

from Comandos import Comandos


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

config = toml.load('config/config.toml')

comando = Comandos()

updater = Updater(config['TOKEN'])

# Registra os comandos
updater.dispatcher.add_handler(CommandHandler('hello', comando.hello))
#updater.dispatcher.add_handler(CommandHandler('reides', comando.reides))
#updater.dispatcher.add_handler(CommandHandler('lista', comando.novaReide))
#updater.dispatcher.add_handler(CommandHandler('amigos', comando.amigos))
updater.dispatcher.add_handler(CommandHandler('ajuda', comando.ajuda))
updater.dispatcher.add_handler(CommandHandler('calc', comando.calc))
#updater.dispatcher.add_handler(CommandHandler('', comando))

updater.start_polling()
updater.idle()
