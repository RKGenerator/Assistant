import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
from transformers.utils import logging
from text_exchange import rawtext2text
from PyQt5.QtCore import QThread
import tts

tokenizer = AutoTokenizer.from_pretrained('models--tinkoff-ai--ruDialoGPT-medium\snapshots\e51fe3a6ea7037f3f53938e3a58ee6e40a82fce3')
model = AutoModelWithLMHead.from_pretrained('models--tinkoff-ai--ruDialoGPT-medium\snapshots\e51fe3a6ea7037f3f53938e3a58ee6e40a82fce3')
history = ''
switch_key = False

def control_panel(status_mode: bool):
    global switch_key, history
    if status_mode and not switch_key:
        tts.va_speak('Режим диалога включен.')
        switch_key = True
        return
    if status_mode and switch_key:
        tts.va_speak('Режим диалога уже активен. Скажите что-нибудь.')
        return
    if not status_mode:
        tts.va_speak('Диалог окончен. Спасибо за внимание. Всего доброго.')
        switch_key = False
        history = ''
        return
'''
def dialog(text: str):
    global history, switch_key
    if not switch_key:
        return
    inputs = tokenizer(history + f'@@ПЕРВЫЙ@@ {text} @@ВТОРОЙ@@', return_tensors='pt')
    generated_token_ids = model.generate(**inputs,
        top_k=10,
        top_p=0.95,
        num_beams=1,
        do_sample=True,
        no_repeat_ngram_size=2,
        temperature=1.2,
        repetition_penalty=1.2,
        length_penalty=1.0,
        eos_token_id=50257,
        pad_token_id=50257,
        max_new_tokens=40
    )
    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    response = context_with_response[0].split('@@ВТОРОЙ@@')[-1].replace('@@ПЕРВЫЙ@@', '')
    history = context_with_response[0]
    history = history[:len(history)-10]
    response = rawtext2text(response)
    tts.va_speak(response)
'''

class dialog(QThread):

    def __init__(self, text:str):
        QThread.__init__(self)
        self.text = text

    def run(self):
        global history, switch_key, tokenizer, model
        if not switch_key:
            return
        inputs = tokenizer(history + f'@@ПЕРВЫЙ@@ {self.text} @@ВТОРОЙ@@', return_tensors='pt')
        generated_token_ids = model.generate(**inputs,
            top_k=10,
            top_p=0.95,
            num_beams=1,
            do_sample=True,
            no_repeat_ngram_size=2,
            temperature=1.2,
            repetition_penalty=1.2,
            length_penalty=1.0,
            eos_token_id=50257,
            pad_token_id=50257,
            max_new_tokens=40
        )
        context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
        response = context_with_response[0].split('@@ВТОРОЙ@@')[-1].replace('@@ПЕРВЫЙ@@', '')
        history = context_with_response[0]
        history = history[:len(history)-10]
        response = rawtext2text(response)
        tts.va_speak(response)