import config

def query_parser(text, cmd: str):
    for item in config.VA_CMD_LIST[cmd]:
            text_splited = text.partition(item+' ')
            if len(text_splited[2]):
                text_splited = text_splited[2]
                return text_splited
    return text

def rawtext2text(text: str):
    dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': '1', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': '2', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': '4', 'ш': 'w', 'щ': '3', 'ъ': '5', 'ы': 'y', 'ь': '6', 'э': '7', 'ю': '8', 'я': '9', '–': '='}
    alph = '_~|!+,-.:;?абвгдежзийклмнопрстуфхцчшщъыьэюяё–…'
    inv_dict = {value: key for key, value in dict.items()}
    for char in range(len(text)):
        if text[char].lower() in dict.keys() or text[char] == ' ' or text[char].lower() in alph:
            continue
        if text[char].lower() in dict.values():
            text = text[:char] + inv_dict[text[char].lower()] + text[char+1:]
            continue
        text = text[:char] + ' ' + text[char+1:]
    return text
