import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def compression(i,o):
    compress(i,o)

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a File: ")
    return filename

def decompression(i,o):
    decompress(i,o)

# Main Window
window = tk.Tk()
window.title("Compression/Decompression Engine")
window.geometry("500x100")

# Button
compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file(),"Compression\compOut1.txt"))
decompress_button = tk.Button(window,text="Decompress",command=lambda:decompression(dec_input_entry.get(),dec_output_entry.get()))

# Entries
# Input
# Compression
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text="Input File: ").grid(row=0,column=0)
input_entry.grid(row=0,column=1)

output_label = tk.Label(window,text="Output File: ").grid(row=1,column=0)
output_entry.grid(row=1,column=1)

compress_button.grid(row=2,column=1)

# Decompression
dec_input_entry = tk.Entry(window)
dec_output_entry = tk.Entry(window)

dec_input_label = tk.Label(window,text="Input File: ").grid(row=0,column=3)
dec_input_entry.grid(row=0,column=4)

dec_output_label = tk.Label(window,text="Output File: ").grid(row=1,column=3)
dec_output_entry.grid(row=1,column=4)

decompress_button.grid(row=2,column=4)


window.mainloop()