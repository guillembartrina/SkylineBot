import os
import pickle
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from cl.treevisitor import parse, Visitor
import random as rand
import re as re

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
namepattern = re.compile("[a-zA-Z0-9]+")


def start(update, context):
    msg = "Hola! Sóc el GBM-SkylineBot, pots usar-me per crear els teus skylines personalitzats"
    if str(update.effective_chat.id) not in os.listdir("."):
        os.mkdir(str(update.message.from_user.id))
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def help(update, context):
    msg = "Comandes disponibles:\n\
/start : inicia el bot\n\
/help : mostra aquesta ajuda\n\
/author : mostra l'informació de l'autor\n\
/lst : llista els skylines definits\n\
/clean : elimina els skylines definits\n\
/save [id] : guarda l'skyline com a id\n\
/load [id] : carrega l'skyline id\n\
/sky : llista els skylines guardats"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def author(update, context):
    msg = "# Guillem Bartrina Moreno\n<guillem.bartrina@est.fib.upc.edu>"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def lst(update, context):
    msg = "Skylines definits: " + str(len(context.user_data)) + "\n"
    for key in context.user_data:
        msg = msg + "· " + key + "\n"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def clean(update, context):
    msg = "<skylines eliminats>"
    context.user_data.clear()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def save(update, context):
    msg = ""
    if(len(context.args) != 1):
        msg = "[mal cridat {usage: /save [id]}]"
    else:
        name = context.args[0]
        if not namepattern.match(name):
            msg = "[nom incorrecte, només alfanumeric]"
        else:
            if name in context.user_data:
                file = open(str(update.effective_chat.id) + "/" + name + ".sky", 'wb')
                pickle.dump(context.user_data[name], file)
                file.close()
                msg = "<guardat>"
            else:
                msg = "[skyline '" + name + "' no definit]"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def load(update, context):
    msg = ""
    if(len(context.args) != 1):
        msg = "[mal cridat {usage: /load [id]}]"
    else:
        name = context.args[0]
        if not namepattern.match(name):
            msg = "[nom incorrecte, només alfanumeric]"
        else:
            try:
                file = open(str(update.effective_chat.id) + "/" + name + ".sky", 'rb')
                context.user_data[name] = pickle.load(file)
                file.close()
                msg = "<carregat>"
            except FileNotFoundError:
                msg = "[skyline '" + name + "' no esta guardat]"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def sky(update, context):
    msg = "Skylines guardats:\n"
    for name in os.listdir(str(update.effective_chat.id) + "/"):
        msg = msg + "· " + name + "\n"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
        )


def msg(update, context):
    text = update.message.text
    if text[0] == '/':
        msg = "[comanda no definida]"
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=msg
            )
    else:
        try:
            Visitor.skylines = context.user_data
            skyline = parse(text)
            context.user_data.update(Visitor.skylines)
            name = "%d.png" % rand.randint(1000, 9999)
            (maxh, area) = skyline.save(name)
            if maxh > 0:
                msg = "àrea: " + str(area) + "\nalçada: " + str(maxh)
                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=open(name, 'rb')
                    )
                os.remove(name)
            else:
                msg = "{skyline buit}"
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=msg
                )

        except Exception as err:
            msg = str(err)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=msg
                )


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('sky', sky))

dispatcher.add_handler(MessageHandler(Filters.text, msg))

updater.start_polling()
