from src.encryption.des_encrypt import encrypt_image
from src.utils.image_processing import load_image, save_image
import os
import unittest
from PIL import Image

class TestImageEncryption(unittest.TestCase):

    def setUp(self):
        self.test_image_path = 'test_image.png'
        self.output_encrypted_path = 'encrypted_image.bin'
        self.key = 'mysecret'  
        self.image = Image.new('RGB', (100, 100), color='red')
        self.image.save(self.test_image_path)

    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists(self.output_encrypted_path):
            os.remove(self.output_encrypted_path)

    def test_encrypt_image(self):
        encrypted_data = encrypt_image(self.test_image_path, self.key)
        self.assertIsInstance(encrypted_data, bytes)
        self.assertGreater(len(encrypted_data), 0)

    def test_encrypt_image_invalid_key(self):
        with self.assertRaises(ValueError):
            encrypt_image(self.test_image_path, 'short')

    def test_encrypt_image_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            encrypt_image('nonexistent_image.png', self.key)

if __name__ == '__main__':
    unittest.main()