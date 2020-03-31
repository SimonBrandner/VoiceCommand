from pynput.keyboard import Key, Controller
import speech_recognition as sr
import json
import time
import sys

Stop = False

def getKeysByVoiceCommand(voiceCommand, data):
    for group in data:
        for command in group["voiceCommands"]:
            if (command in voiceCommand):
                return group["keysToPress"]
    return "Error"

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

def handleVoiceCommand(recognizer, audio):
    print("Trying to recognize what you said.")
    try:
        voiceCommand = r.recognize_google(audio)
        if (voiceCommand == "exit"): 
            print("Exit command called")
            global Stop
            Stop = True

        print("You said: " + voiceCommand)

        keys = getKeysByVoiceCommand(voiceCommand, data)
        if (not(keys == "Error")):
            pressAppropriateKeys(keys)
            releaseAppropriateKeys(keys)
        else:
            print("That's unknown command")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print("You may speak.")

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

    with mic as source:
        r.adjust_for_ambient_noise(source)

    stopListening = r.listen_in_background(mic, handleVoiceCommand)
    
    print("You may speak.")

    while (Stop == False):
        pass
    
    stopListening()