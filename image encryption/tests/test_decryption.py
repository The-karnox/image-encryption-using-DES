from src.encryption.des_decrypt import decrypt_image
from src.utils.image_processing import load_image, save_image
import os
import unittest
from PIL import Image

class TestDecryption(unittest.TestCase):
    
    def setUp(self):
        self.key = "mysecret"  # Example key, should be 8 bytes for DES
        self.test_image_path = "test_image.png"
        self.encrypted_image_path = "encrypted_image.dat"
        self.decrypted_image_path = "decrypted_image.png"
        
        # Load and encrypt the test image for testing
        original_image = load_image(self.test_image_path)
        encrypted_data = self.encrypt_image(original_image, self.key)
        with open(self.encrypted_image_path, 'wb') as f:
            f.write(encrypted_data)

    def encrypt_image(self, image, key):
        from src.encryption.des_encrypt import encrypt_image
        return encrypt_image(image, key)

    def test_decrypt_image(self):
        with open(self.encrypted_image_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_image = decrypt_image(encrypted_data, self.key)
        save_image(decrypted_image, self.decrypted_image_path)

        # Verify that the decrypted image matches the original
        original_image = load_image(self.test_image_path)
        self.assertTrue(self.images_are_equal(original_image, decrypted_image))

    def images_are_equal(self, img1, img2):
        return list(img1.getdata()) == list(img2.getdata())

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.encrypted_image_path):
            os.remove(self.encrypted_image_path)
        if os.path.exists(self.decrypted_image_path):
            os.remove(self.decrypted_image_path)

if __name__ == '__main__':
    unittest.main()