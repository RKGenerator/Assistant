from PyQt5.QtCore import QThread
import torch
import sounddevice as sd
import time

class TTS(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.language = 'ru'
        self.model_id = 'ru_v3'
        self.sample_rate = 48000 # 48000
        self.speaker = 'aidar' # aidar, baya, kseniya, xenia, random
        self.put_accent = True
        self.put_yo = True
        #self.device = torch.device('cpu') # cpu или gpu

        self.model, _ = torch.hub.load(repo_or_dir='snakers4_silero-models_master',
                                  source='local',
                                  model='silero_tts',
                                  language=self.language,
                                  speaker=self.model_id)
        #self.model.to(self.device)
        self.what = ''

    def run(self):
        while not self.isInterruptionRequested():
            if self.what:
                if len(self.what) > 140:
                    text_list = []
                    for index in range(0, 140*(len(self.what)//140+1), 140):
                        text_list.append(self.what[index:index+140])
                    for count in range(0, len(text_list)):
                        audio = self.model.apply_tts(text=text_list[count],
                                                speaker=self.speaker,
                                                sample_rate=self.sample_rate,
                                                put_accent=self.put_accent,
                                                put_yo=self.put_yo)

                        sd.play(audio, self.sample_rate * 1.05)
                        time.sleep((len(audio) / self.sample_rate))
                else:
                    audio = self.model.apply_tts(text=self.what,
                                                speaker=self.speaker,
                                                sample_rate=self.sample_rate,
                                                put_accent=self.put_accent,
                                                put_yo=self.put_yo)
                    sd.play(audio, self.sample_rate * 1.05)
                    time.sleep((len(audio) / self.sample_rate) + 0.5)
                    #time.sleep((len(audio) / sample_rate) + 0.5)
                sd.stop()
                self.what = ''








gui = None
def tts_gui_init(gui_class):
    global gui 
    gui = gui_class

def va_speak(what: str):
    global gui
    gui.bot_message(what)
    gui.tts.what = what
