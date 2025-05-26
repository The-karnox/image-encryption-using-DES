from encryption.des_encrypt import encrypt_image
from encryption.des_decrypt import decrypt_image
from utils.image_processing import load_image, save_image
import sys

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <encrypt/decrypt> <image_path> <key> [output_path]")
        return

    operation = sys.argv[1]
    image_path = sys.argv[2]
    key = sys.argv[3]

    if operation == "encrypt":
        encrypted_data = encrypt_image(image_path, key)
        output_path = sys.argv[4] if len(sys.argv) > 4 else "encrypted_image.dat"
        with open(output_path, "wb") as f:
            f.write(encrypted_data)
        print(f"Image encrypted and saved to {output_path}")

    elif operation == "decrypt":
        output_path = sys.argv[4] if len(sys.argv) > 4 else "decrypted_image.png"
        with open(image_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_image = decrypt_image(encrypted_data, key)
        save_image(decrypted_image, output_path)
        print(f"Image decrypted and saved to {output_path}")

    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()