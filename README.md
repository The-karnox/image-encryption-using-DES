# Image Encryption using DES

This project implements image encryption and decryption using the Data Encryption Standard (DES) algorithm. It aims to ensure the confidentiality and integrity of digital images during transmission or storage.

## Objectives

1. Understand the DES algorithm and its applicability to image encryption.
2. Develop a software system to encrypt digital images using DES.
3. Implement a decryption module to reconstruct the original image from its encrypted version.
4. Ensure the image retains its original quality and resolution after decryption.
5. Evaluate the performance of DES in terms of speed, data integrity, and resistance to basic attacks.
6. Compare the original and decrypted images to validate the success of the encryption process.

## Project Structure

```
image-encryption-des
├── src
│   ├── encryption
│   │   ├── des_encrypt.py      # Implementation of the DES encryption algorithm
│   │   └── des_decrypt.py      # Implementation of the DES decryption algorithm
│   ├── utils
│   │   └── image_processing.py  # Utility functions for image handling
│   └── main.py                 # Entry point for the application
│   └── gui_app.py              # Entry point for the application execution
├── tests
│   ├── test_encryption.py      # Unit tests for the encryption functionality
│   └── test_decryption.py      # Unit tests for the decryption functionality
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files and directories to ignore in version control

```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To encrypt an image, run the following command:

```
python src/main.py encrypt <image_path> <key>
```

To decrypt an image, run:

```
python src/main.py decrypt <encrypted_image_path> <key>
```

## DES Algorithm

The Data Encryption Standard (DES) is a symmetric-key algorithm for the encryption of digital data. It uses a fixed-size key and operates on blocks of data, making it suitable for encrypting images.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.