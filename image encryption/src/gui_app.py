import tkinter as tk
from tkinter import filedialog, messagebox
from src.encryption.des_encrypt import encrypt_image

def encrypt_action():
    img_path = filedialog.askopenfilename(title="Select Image")
    if not img_path:
        return
    key = key_entry.get()
    if len(key) != 8:
        messagebox.showerror("Error", "Key must be 8 characters long.")
        return
    try:
        encrypted_data = encrypt_image(img_path, key)
        save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
        if save_path:
            with open(save_path, "wb") as f:
                f.write(encrypted_data)
            messagebox.showinfo("Success", f"Image encrypted and saved as:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image DES Encryptor")

tk.Label(root, text="DES Key (8 chars):").pack(pady=5)
key_entry = tk.Entry(root, show="*")
key_entry.pack(pady=5)

tk.Button(root, text="Encrypt Image", command=encrypt_action).pack(pady=10)

root.mainloop()