import os
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
from PIL import Image, ImageTk

RED = "#C21010"
GREEN = "#285430"
WHITE = "#FFFDE3"
FONT_NAME = "Courier"
input_file_1 = ""
input_file_2 = ""

# Generate a Fernet key
key = b'48avIhEHGl8wAuBVBsXeUkSdGeNn3OzqKLFn8TT1gU4='

# Create a Fernet instance with the key
fernet = Fernet(key)

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title("Image Encryption and Decryption")
window.config(width=600, height=420, bg=WHITE)

def encrypt_upload_image():

    global input_file_1
    # Ask the user to select an image file
    input_file_1 = filedialog.askopenfilename()

def decrypt_upload_image():
        
    global input_file_2
    # Ask the user to select an image file
    input_file_2 = filedialog.askopenfilename()    

# Function to encrypt an image
def encrypt_image():

    # Open the image file in binary mode
    with open(input_file_1, "rb") as f:
        # Read the image file contents
        image_bytes = f.read()

        # Encrypt the image bytes
        encrypted_bytes = fernet.encrypt(image_bytes)

        # Save the encrypted image to a file
        encrypted_file = filedialog.asksaveasfilename(defaultextension='.png')

        # Write the encrypted bytes to file
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_bytes)          

# Function to decrypt an image
def decrypt_image():

    # Decrypt the image
    with open(input_file_2, "rb") as f:
        # Read the encrypted file contents
        encrypted_bytes = f.read()

        # Decrypt the image bytes
        decrypted_bytes = fernet.decrypt(encrypted_bytes)

        # Save the decrypted image to a file
        decrypted_file = filedialog.asksaveasfilename(defaultextension='.png')

        # Write the decrypted bytes to file
        with open(decrypted_file, "wb") as f:
            f.write(decrypted_bytes)             

# Create a title for the encryption section
enc_title = tk.Label(text="Encrypting Image", bg=WHITE, fg=GREEN, font=(FONT_NAME, 18), padx=10, pady=10)
enc_title.place(x=180, y=20)

# Create a button to upload an image
upload_button = tk.Button(text="Upload Image", padx=5, pady=5, command=encrypt_upload_image)
upload_button.place(x=250, y=80)

# Create a button to encrypt an image
encrypt_button = tk.Button(text="Encrypt Image", padx=5, pady=5, command=encrypt_image)
encrypt_button.place(x=250, y=130)

# Create a title for the decryption section
dec_title = tk.Label(text="Decrypting Image", bg=WHITE, fg=RED, font=(FONT_NAME, 18), padx=10, pady=10)
dec_title.place(x=180, y=210)

# Create a button to upload an image
upload_button = tk.Button(text="Upload Image", padx=5, pady=5, command=decrypt_upload_image)
upload_button.place(x=250, y=270)

# Create a button to decrypt an image
decrypt_button = tk.Button(text="Decrypt Image", padx=5, pady=5, command=decrypt_image)
decrypt_button.place(x=250, y=320) 

# Start the Tkinter event loop
window.mainloop()    