from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from PIL import Image
import io

def encrypt_image(image_path: str, key: str) -> bytes:
    # Ensure the key is exactly 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long.")
    
    # Load the image
    image = Image.open(image_path)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=image.format)
    image_data = image_bytes.getvalue()
    
    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC)
    
    # Pad the image data to be a multiple of 8 bytes
    padded_data = pad(image_data, DES.block_size)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Prepend the IV to the encrypted data for decryption
    return cipher.iv + encrypted_data