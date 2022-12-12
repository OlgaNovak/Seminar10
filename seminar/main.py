from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

bot=Bot(token='5983794487:AAE_UGHcZ75SpotFykyW8CaP--WfiXeJmxA')
updater=Updater(token='5983794487:AAE_UGHcZ75SpotFykyW8CaP--WfiXeJmxA')
dispahather=updater.dispatcher

def start(update,context):
    context.bot.send_message(update.effective_chat.id,"Введите ваше выражение")

def main(update,context):
    text=update.message.text
    a=parse(text)
    b=calculate(a)
    loger(text,b)
    context.bot.send_message(update.effective_chat.id,f'Результат вычисления: {b}')

   
def loger(text,result):
    with open ('file.txt','a') as data:
        #logger=logging.getLogger(__name__)
        rasparse="".join(map(str,text))
        rasparse=rasparse+"="
        result=str(result)+';\n'
        #data.write(str(logger))
        data.write(str(rasparse))
        data.write(str(result))
        

def parse(s):
    result=[]
    digit=" "
    for symbol in s:
        if symbol.isdigit():
            digit+=symbol
        else:
            result.append(int(digit))
            digit=" "
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result


def calculate(lst):
    result=0.0
    for s in lst:
        if s=='*' or s=='/':
            if s=='*':
                index=lst.index(s)
                result=lst[index-1]*lst[index+1]
                lst=lst[:index-1]+[result]+lst[index+2:]
            else:
                index=lst.index(s)
                result=lst[index-1]/lst[index+1]
                lst=lst[:index-1]+[result]+lst[index+2:]
    for s in lst:
        if s=='+' or s=='-':
            if s=='+':
                index=lst.index(s)
                result=lst[index-1]+lst[index+1]
                lst=lst[:index-1]+[result]+lst[index+2:]
            else:
                index=lst.index(s)
                result=lst[index-1]-lst[index+1]
                lst=lst[:index-1]+[result]+lst[index+2:]
    return result

          
start_handler=CommandHandler("Hello",start)
message_handler=MessageHandler(Filters.text, main)


dispahather.add_handler(start_handler)
dispahather.add_handler(message_handler)

updater.start_polling()
updater.idle()
