from pynput.keyboard import Key, Controller
import speech_recognition as sr
import json
import time
import sys

def getKeysByVoiceCommand(voiceCommand, data):
    for group in data:
        for command in group["voiceCommands"]:
            if (command == voiceCommand):
                return group["keysToPress"]

def pressAppropriateKeys(keys):
    for key in keys:
        if(key == "shift"):
            keyboard.press(Key.shift)
        elif(key == "ctrl"):
            keyboard.press(Key.ctrl)
        elif(key == "alt"):
            keyboard.press(Key.alt)
        elif(key == "cmd"):
            keyboard.press(Key.cmd)
        elif(key == "insert"):
            keyboard.press(Key.insert)
        elif(key == "up"):
            keyboard.press(Key.up)
        elif(key == "down"):
            keyboard.press(Key.down)
        elif(key == "left"):
            keyboard.press(Key.left)
        elif(key == "right"):
            keyboard.press(Key.right)
        elif(key == "home"):
            keyboard.press(Key.home)
        else:
            keyboard.press(key)

def releaseAppropriateKeys(keys):
    for key in keys:
        if(key == "shift"):
            keyboard.release(Key.shift)
        elif(key == "ctrl"):
            keyboard.release(Key.ctrl)
        elif(key == "alt"):
            keyboard.release(Key.alt)
        elif(key == "cmd"):
            keyboard.release(Key.cmd)
        elif(key == "insert"):
            keyboard.release(Key.insert)
        elif(key == "up"):
            keyboard.release(Key.up)
        elif(key == "down"):
            keyboard.release(Key.down)
        elif(key == "left"):
            keyboard.release(Key.left)
        elif(key == "right"):
            keyboard.release(Key.right)
        elif(key == "home"):
            keyboard.release(Key.home)
        else:
            keyboard.release(key)

if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()
    keyboard = Controller()

    if (len(sys.argv) < 2):
        sys.exit("You haven't provided any config file!")
    try:
        data = json.load(open(sys.argv[1]))
    except Exception as e: 
        sys.exit(e)

    while(True):
        with mic as source:
            audio = r.listen(source)
            try:
                voiceCommand = r.recognize_google(audio)
                if (voiceCommand == "quit"): break
                print(voiceCommand)

                keys = getKeysByVoiceCommand(voiceCommand, data)

                pressAppropriateKeys(keys)
                releaseAppropriateKeys(keys)

            except Exception as e: 
                print(e)