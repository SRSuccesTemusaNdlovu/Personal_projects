from gtts import gTTS
import os
from tkinter import *

def text_to_speech():
    text = text_box.get("1.0", END).strip()  
    if text:
        language = "en"
        output = gTTS(text=text, lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")

def main():
    root = Tk()
    root.title("Text to Speech Converter")
    canvas = Canvas(root, width=400, height=300)
    canvas.pack()

    # Add label
    label = Label(root, text="Text to Speech Converter", font=("Helvetica", 16))
    canvas.create_window(200, 50, window=label)

    # Text widget for multi-line input
    global text_box
    text_box = Text(root, wrap=WORD, width=40, height=10)
    canvas.create_window(200, 150, window=text_box)

    # Button to start conversion
    button = Button(text="Start", command=text_to_speech)
    canvas.create_window(200, 260, window=button)

    root.mainloop()

if __name__ == '__main__':
    main()
