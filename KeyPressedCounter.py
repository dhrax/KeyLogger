from genericpath import exists
from pynput import keyboard
import json
import os
from pathlib import Path

"""todo
añadir el programa a que se inicie cada vez que se inicie sesion
cuando finalice el programa, grabar los datos del diccionario
grabar datos acumulados en varias ejecuciones
"""

dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'ñ': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

LogDirectory = "\\Logs\\"
filename = ""

def on_key_release(key):
    if key == keyboard.Key.esc:
        writeLog(filename)
    else:
        try:
            dict[key.char] += 1
        except:
            print("Excepcion")


def main():
    setLogname()
    initLog(filename)
    initDict(filename)
    initListener()

def setLogname():
    #filename = __file__
    global filename
    filename = os.path.basename(__file__)
    filename = filename[0:filename.find('.')] + ".json"

    dir_path = os.path.dirname(os.path.realpath(__file__)) + LogDirectory
    filename = dir_path + filename

def initListener():
    with keyboard.Listener(on_release = on_key_release) as listener:
        listener.join()

def initLog(filename):
    if not exists(filename):
        Path(filename).touch()
        writeLog(filename)        

def writeLog(file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

def initDict(file):
    with open(file, 'r') as fp:
        dict = json.load(fp)

if __name__ == '__main__':
    main()