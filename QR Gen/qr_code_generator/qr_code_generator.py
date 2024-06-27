from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    
    # Generate QR code
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    
    # Open the generated QR code image using PIL
    qr_image = Image.open(file_name)
    qr_code_image = ImageTk.PhotoImage(qr_image)
    
    # Display the QR code image in a label on the canvas
    image_label.config(image=qr_code_image)
    image_label.image = qr_code_image  # Keep a reference to the image to prevent garbage collection
    
    canvas.create_window(200, 400, window=image_label)

def main():
    root = Tk()
    root.title("QR Code Generator")

    # Creating canvas
    canvas = Canvas(root, width=400, height=600)
    canvas.pack()

    # Creating title
    app_label = Label(root, text="QR Code Generator", font=("Helvetica", 16))
    canvas.create_window(200, 50, window=app_label)

    # Creating labels 'Link Name' and 'Link'
    name_label = Label(root, text="Link name ")
    link_label = Label(root, text="Link " )
    canvas.create_window(200, 100, window=name_label)
    canvas.create_window(200, 160, window=link_label)

    # Creating entry boxes
    global name_entry, link_entry, image_label
    name_entry = Entry(root)
    link_entry = Entry(root)
    canvas.create_window(200, 130, window=name_entry)
    canvas.create_window(200, 180, window=link_entry)

    # Creating button to generate QR code
    button = Button(text="Generate QR code", command=generate)
    canvas.create_window(200, 230, window=button)

    # Creating label to display QR code image
    image_label = Label(root)
    canvas.create_window(200, 350, window=image_label)

    root.mainloop()

if __name__ == '__main__':
    main()
