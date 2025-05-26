import tkinter as tk
from tkinter import filedialog, messagebox
from src.encryption.des_encrypt import encrypt_image
from src.encryption.des_decrypt import decrypt_image

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

def decrypt_action():
    bin_path = filedialog.askopenfilename(title="Select Encrypted File", filetypes=[("Binary files", "*.bin")])
    if not bin_path:
        return
    key = key_entry.get()
    if len(key) != 8:
        messagebox.showerror("Error", "Key must be 8 characters long.")
        return
    try:
        with open(bin_path, "rb") as f:
            encrypted_data = f.read()
        image = decrypt_image(encrypted_data, key)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Success", f"Image decrypted and saved as:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image DES Encryptor/Decryptor")

tk.Label(root, text="DES Key (8 chars):").pack(pady=5)
key_entry = tk.Entry(root, show="*")
key_entry.pack(pady=5)

tk.Button(root, text="Encrypt Image", command=encrypt_action).pack(pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_action).pack(pady=10)

root.mainloop()