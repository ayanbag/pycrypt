# PyCrypt

A collection of **cryptographic algorithms** like Reverse Cipher , Caeser Cipher and many more to be used in encryption srcipts.

# Algoritms include:

Till now I am able include only a handfull of cryptograhic algoritms and looking forward to add more.The algorithms included in PyCrypt package :
* Reverse Cipher
* Caeser Cipher
* ROT13 Cipher
* XOR Cipher
* Affine Cipher
* Viginere Cipher

# Installation

From Pypi:

Make sure you're using `python3` and have `pip` installed and enabled. On the command line, simply run:

`pip install PyCrypt`

And From GitHub Repo:

clone the repository

`git clone https://github.com/ayanbag/pycrypt.git`

Navigate into the project directory

`cd pycrypt`

Install pydl and its dependencies

`python setup.py install`


# Tutorials

To use **PyCrypt** in your programs, you have to import it : 

`import pycrypt`


* Reverse Cipher:

`pycrypt.reverse.cipher(message)`

where, message -> It is a set of characters or strings which you want to encrypt.

* Caeser Cipher:

`pycrypt.caesar_cipher(message,encode=False,decode=False)`

where, message ->(string) It is a set of characters or strings which you want to encrypt or decrypt.
encode ->(Boolean) Set *True* if you want to encrypt the current message.By default it is *False*.
decode ->(Boolean) Set *True* if you want to decrypt the current cipher text.By default it is *False*.

* ROT13 Cipher:

`pycrypt.rot13_cipher(message)`

where
