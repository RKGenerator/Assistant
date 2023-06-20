import vosk
import sys
import sounddevice as sd
import queue
import json
from PyQt5.QtCore import QThread
from AI import va_respond

class STT (QThread):
    
    def __init__(self):
        QThread.__init__(self)
        self.model = vosk.Model('model_small')
        self.samplerate = 16000
        self.device = sd.query_devices(kind='input')['index']

        self.q = queue.Queue()

    def run(self):
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.device, dtype='int16',
                               channels=1, callback=self.q_callback) as stream:
            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            while not self.isInterruptionRequested():
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    va_respond(json.loads(rec.Result())["text"])
            else:
                stream.stop()

    def q_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

