from telegram.ext import Updater, CallbackContext
from math import ceil

class Comandos:
    def __ini__(self):
        pass

    def hello(self, update: Updater, context: CallbackContext) -> None:
        update.message.reply_text(f'Hello {update.effective_user.first_name}')

    def reides(self, update: Updater, context: CallbackContext) -> None:
        pass

    def novaReide(self, update: Updater, context: CallbackContext) -> None:
        pass

    def amigos(self, update: Updater, context: CallbackContext) -> None:
        pass

    def calc(self, update: Updater, context: CallbackContext) -> None:
        calcular = update.message.text
        if len(calcular) > 5:
            atk, defe, ps = calcular[5:].strip().split('/')
            IV = ceil((int(atk) + int(defe) + int(ps)) * 2.2)
            update.message.reply_text(f'IV: {IV}%')
        else:
            update.message.reply_text("Verifique se você passou os valores de atk/def/ps")

    def ajuda(self, update: Updater, context: CallbackContext) -> None:
        update.message.reply_text("""
        Olá, esses são os comandos e como usa-los:
/calc atk/def/ps - calcula o IV do pokemon 
/reides - mostra as listas das reides disponiveis para fazer.
/lista - Cria uma nova lista de reide.
/amigos - mostra o link da lista de amigos do grupo.
/ajuda - mostra essa mensagem.
        """)

