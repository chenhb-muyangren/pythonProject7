from PyQt5.QtCore import *

class main_windows(QObject):
    sendmeg=pyqtSignal(str)
    def send(self):
        self.sendmeg.emit('hello world')

class UI_windows(QObject):
    def get(self,msg):
        print(msg)

if __name__ == '__main__':
    send=main_windows()
    slot=UI_windows()
    send.sendmeg.connect(slot.get)
    send.send()