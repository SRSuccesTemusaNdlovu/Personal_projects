import tkinter as tk
from tkinter import filedialog
import zlib
import base64

def open_file(entry_widget):
    file_name = filedialog.askopenfilename(initialdir='/Desktop', title="Select a file")
    entry_widget.delete(0, tk.END)  # Clear current content in entry
    entry_widget.insert(0, file_name)  # Insert the selected file path

def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", initialdir='/Desktop', title="Save file as")
    return file_name

def compress(inputfile, outputfile):
    data = open(inputfile, "rb").read()
    compressed_data = base64.b64encode(zlib.compress(data))
    with open(outputfile, "wb") as compressed_file:
        compressed_file.write(compressed_data)

def decompress(inputfile, outputfile):
    file_content = open(inputfile, "rb").read()
    decoded_data = base64.b64decode(file_content)
    decompressed_data = zlib.decompress(decoded_data)
    with open(outputfile, 'wb') as file:
        file.write(decompressed_data)

def compression():
    input_file = input_entry.get()
    output_file = save_file()  # Ask the user where to save the compressed file
    if output_file:  # Check if a file name was provided
        try:
            compress(input_file, output_file)
            status_label.config(text="File compressed successfully!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")

def decompression():
    input_file = input_entry1.get()
    output_file = save_file()  # Ask the user where to save the decompressed file
    if output_file:  # Check if a file name was provided
        try:
            decompress(input_file, output_file)
            status_label.config(text="File decompressed successfully!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")

def main():
    window = tk.Tk()
    window.title("Compression Engine")
    window.geometry("600x400")

    # Create and place widgets for compression
    input_label = tk.Label(window, text="File to be compressed:")
    input_label.grid(row=0, column=0, padx=10, pady=10)
    global input_entry
    input_entry = tk.Entry(window, width=40)
    input_entry.grid(row=0, column=1, padx=10, pady=10)
    input_browse_button = tk.Button(window, text="Browse", command=lambda: open_file(input_entry))
    input_browse_button.grid(row=0, column=2, padx=10, pady=10)

    output_label = tk.Label(window, text="Name of compressed file:")
    output_label.grid(row=1, column=0, padx=10, pady=10)
    global output_entry
    output_entry = tk.Entry(window, width=40)
    output_entry.grid(row=1, column=1, padx=10, pady=10)

    compress_button = tk.Button(window, text="Compress", command=compression)
    compress_button.grid(row=2, column=1, pady=10)

    # Create and place widgets for decompression
    input_label1 = tk.Label(window, text="File to be decompressed:")
    input_label1.grid(row=3, column=0, padx=10, pady=10)
    global input_entry1
    input_entry1 = tk.Entry(window, width=40)
    input_entry1.grid(row=3, column=1, padx=10, pady=10)
    input_browse_button1 = tk.Button(window, text="Browse", command=lambda: open_file(input_entry1))
    input_browse_button1.grid(row=3, column=2, padx=10, pady=10)

    output_label1 = tk.Label(window, text="Name of decompressed file:")
    output_label1.grid(row=4, column=0, padx=10, pady=10)
    global output_entry1
    output_entry1 = tk.Entry(window, width=40)
    output_entry1.grid(row=4, column=1, padx=10, pady=10)

    decompress_button = tk.Button(window, text="Decompress", command=decompression)
    decompress_button.grid(row=5, column=1, pady=10)

    # Status label to display messages
    global status_label
    status_label = tk.Label(window, text="")
    status_label.grid(row=6, column=0, columnspan=3, pady=20)

    window.mainloop()

if __name__ == '__main__':
    main()
