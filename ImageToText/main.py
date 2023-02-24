import os
import pyttsx3

def speak(audio):
    '''
    This function will speak or rather pronounce the argument which you will give it.
    '''
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 198)
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()
    
if __name__ == '__main__':
    os.system("cls")  
    os.system("tesseract image1.png textFile")
    with open("textFile.txt", "r") as f:
        content = f.read()
        print(content)
        speak(content)