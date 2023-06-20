import config
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
import random
from wiki import wiki
from text_exchange import query_parser
import conversations


def va_respond(voice: str):
    if voice == '':
        return
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd, text = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'], query_parser(text, cmd['cmd']))
    else:
        dialog_thread = conversations.dialog(voice)
        dialog_thread.start()


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc, cmd


def execute_cmd(cmd, text: str):
    if cmd == 'help':
        # help
        text = "Я умею: "
        text += "произносить время, "
        text += "рассказывать анекдоты, "
        text += "открывать браузер, "
        text += "отвечать на вопросы, "
        text += "вести диалог. "
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейчас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «можно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        webbrowser.open("https://www.google.com/")

    elif cmd == 'open_vk':
        webbrowser.open("https://vk.com/")

    elif cmd == 'open_youtube':
        webbrowser.open("https://www.youtube.com/")

    elif cmd == 'wiki_search':
        wiki(text)
    
    elif cmd == 'google_search':
        webbrowser.open("https://www.google.com/search?q="+text)

    elif cmd == 'start_dialog':
        conversations.control_panel(True)

    elif cmd == 'end_dialog':
        conversations.control_panel(False)
