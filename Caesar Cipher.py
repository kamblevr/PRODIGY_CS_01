import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Caesar Cipher Functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# GUI App
root = tk.Tk()
root.title("Caesar Cipher - GUI")
root.geometry("500x450")
root.configure(bg="#1e1e2e")

# Title Label
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#89b4fa")
title_label.pack(pady=20)

# Message Entry
msg_label = tk.Label(root, text="Enter Message:", font=("Arial", 12), bg="#1e1e2e", fg="#cdd6f4")
msg_label.pack()
msg_entry = tk.Entry(root, width=40, font=("Arial", 12))
msg_entry.pack(pady=10)

# Shift Value
shift_label = tk.Label(root, text="Enter Shift Value:", font=("Arial", 12), bg="#1e1e2e", fg="#cdd6f4")
shift_label.pack()
shift_entry = tk.Entry(root, width=10, font=("Arial", 12))
shift_entry.pack(pady=10)

# Output Box
output_label = tk.Label(root, text="Output:", font=("Arial", 12), bg="#1e1e2e", fg="#cdd6f4")
output_label.pack()
output_box = tk.Text(root, height=5, width=45, font=("Arial", 12))
output_box.pack(pady=10)

# Functions for Buttons
def encrypt_text():
    try:
        text = msg_entry.get()
        shift = int(shift_entry.get())
        cipher = encrypt(text, shift)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, cipher)
    except:
        messagebox.showerror("Error", "Shift must be a number!")

def decrypt_text():
    try:
        text = msg_entry.get()
        shift = int(shift_entry.get())
        plain = decrypt(text, shift)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, plain)
    except:
        messagebox.showerror("Error", "Shift must be a number!")

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=15)

# Encrypt Button
encrypt_btn = tk.Button(btn_frame, text="Encrypt", width=12, font=("Arial", 12, "bold"), bg="#89b4fa", fg="#1e1e2e", command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=10)

# Decrypt Button
decrypt_btn = tk.Button(btn_frame, text="Decrypt", width=12, font=("Arial", 12, "bold"), bg="#f38ba8", fg="#1e1e2e", command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=10)

root.mainloop()
