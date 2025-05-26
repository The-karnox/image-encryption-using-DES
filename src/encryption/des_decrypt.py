from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
from PIL import Image
import io

def decrypt_image(encrypted_data: bytes, key: str) -> Image:
    # Ensure the key is 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long.")

    # Extract the IV (first 8 bytes)
    iv = encrypted_data[:8]
    encrypted_image_data = encrypted_data[8:]

    # Create a DES cipher object in CBC mode with the extracted IV
    des = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)

    # Decrypt and unpad the data
    decrypted_padded_data = des.decrypt(encrypted_image_data)
    decrypted_data = unpad(decrypted_padded_data, DES.block_size)

    # Convert decrypted bytes back to an image
    image = Image.open(io.BytesIO(decrypted_data))
    return image