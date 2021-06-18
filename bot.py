from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


API_KEY="1811011576:AAGgcFQbl-b2_QrkCE91VLUXPnhE7jCS7LQ"

def start(update, context):
    update.message.reply_text("Welcome to my sample bot")

def download(update, context):
    update.message.reply_text("The file is downloading")
    context.bot.sendDocument(update.effective_chat.id, "https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf")

def EP(update, context):
    update.message.reply_text("The file is downloading")
    context.bot.sendDocument(update.effective_chat.id, "https://iitbhu.ac.in/contents/app/doc/RevisedProgrammeBookletofEnggPhysicssept201.pdf")
    
def calender(update, context):
    update.message.reply_text("The file is downloading")
    context.bot.sendDocument(update.effective_chat.id, "https://iitbhu.ac.in/sites/default/files/institute/academics/academic_info/doc/calendar_20-21_even_only_I-year.pdf")

def download3(update, context):
    update.message.reply_text("The file is downloading")
    context.bot.sendDocument(update.effective_chat.id, "https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf")

def download4(update, context):
    update.message.reply_text("The file is downloading")
    context.bot.sendDocument(update.effective_chat.id, "https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf")


def handle_message(update,context):
    text=str(update.message.text).lower()
    response=R.sample_responses(text)

def error(update, context):
    print(f"Update {update} caused error {context.error}")
 


def main():
    updater= Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("download",download))
    dp.add_handler(CommandHandler("EP",EP))
    dp.add_handler(CommandHandler("calender",calender))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()
