import wikipedia
import tts
import numpy as np
import config
from text_exchange import rawtext2text


wikipedia.set_lang('ru')

def wiki(text: str):
    try:
        answer = wikipedia.summary(text).partition('\n')[0]
        answer = rawtext2text(answer)
        tts.va_speak(answer)
    except wikipedia.exceptions.DisambiguationError as error:
        tts.va_speak('Вы указали неоднозначное определене. Пожалуйста сгенерируйте запрос занова выбрав одно из следующих определений:')
        for item in error.options:
            tts.va_speak(rawtext2text(item))
    except wikipedia.exceptions.HTTPTimeoutError:
        tts.va_speak('Извините, отсутсвует подключение к интернету. Попробуйте позже.')
    except wikipedia.exceptions.PageError:
        tts.va_speak('Извините, но на данный момент я не располагаю необходимыми данными чтобы удовлетворить этот запрос')
    except (wikipedia.exceptions.RedirectError, wikipedia.exceptions.WikipediaException):
        tts.va_speak('Извините, произошла ошибка поиска. Попробуйте позже.')