import os
import pyttsx3
import cv2
from string import printable
import fontstyle as fnt
from PIL import Image, ImageFilter

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

def capture(image_name):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    
    # reading the input using the camera
    result, image = cam.read()
    
    # If image will detected without any error, 
    # show result
    if result:
        # showing result, it take frame name and image 
        # output
        cv2.imshow(image_name, image)
        # saving image in local storage
        cv2.imwrite(f"{image_name}.png", image)
        # If keyboard interrupt occurs, destroy image 
        # window
       
        cv2.destroyWindow(image_name)
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

if __name__ == '__main__':
    os.system("cls")
    image_path = "image.png"
    capture("image")
    
    # Open the image file
    image = Image.open('image.png')

    # Sharpen the image using the UnsharpMask filter
    sharpened_image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    # Save the sharpened image
    sharpened_image.save('new_image.png')
    
    # os.system(f"tesseract {image_path} outputFile")
    os.system(f"tesseract new_image.png outputFile")
    with open("outputFile.txt") as text_file:
        text = text_file.read()
    
    text_list = text.split(" ")
    for item in text_list:
        if item not in printable:
            text.replace(item, "")
    
    os.system("cls")
    print(fnt.apply(text, "blue/bold"))
    speak(text)
    # os.remove("outputFile.txt")
    # os.remove(image_path)
