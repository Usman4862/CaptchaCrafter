import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button, Frame
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha

def create_image(flag=0):
    global random_string, image_label, image_display, entry, verify_label
    
    if flag == 1:
        verify_label.config(text="")
    
    entry.delete(0, tk.END)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    image_captcha = ImageCaptcha(width=250, height=100)
    image_generated = image_captcha.generate(random_string)
    image_display = ImageTk.PhotoImage(Image.open(image_generated))
    
    image_label.config(image=image_display)
    image_label.image = image_display

def check_input():
    global verify_label
    if entry.get().strip().lower() == random_string.lower():
        verify_label.config(text="✅ Verified!", fg="#00a806")
    else:
        verify_label.config(text="❌ Incorrect!", fg="#fa0800")
        create_image()


root = tk.Tk()
root.title("Unique Captcha Generator")
root.geometry("420x350")
root.configure(background="#e3edf7")

# Main Frame with Glassmorphism Effect
main_frame = Frame(root, bg="#ffffff", bd=5, relief="ridge")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

Label(main_frame, text="🔐 Enter Captcha", font=("Arial", 15, "bold"), bg="#ffffff").pack(pady=10)

image_label = Label(main_frame, bg="#f8f9fa", relief="solid", bd=2, width=250, height=100)
image_label.pack(pady=10)

entry = Entry(main_frame, width=12, font=("Arial", 16), justify="center", bd=3, relief="ridge")
entry.pack(pady=10)

btn_frame = Frame(main_frame, bg="#ffffff")
btn_frame.pack(pady=5)

reload_img = ImageTk.PhotoImage(Image.open("refresh.png").resize((32, 32), Image.LANCZOS))
reload_button = Button(btn_frame, image=reload_img, command=lambda: create_image(1), bd=2, relief="raised", bg="#ffffff")
reload_button.grid(row=0, column=0, padx=10)

submit_button = Button(btn_frame, text="Submit", font=("Arial", 12, "bold"), bg="#007BFF", fg="white", bd=3, relief="raised", command=check_input)
submit_button.grid(row=0, column=1, padx=10)

verify_label = Label(main_frame, text="", font=("Arial", 14), bg="#ffffff")
verify_label.pack(pady=10)

create_image()

root.mainloop()
