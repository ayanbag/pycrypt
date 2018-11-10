# PyCrypt

A collection of **cryptographic algorithms** like Reverse Cipher , Caeser Cipher and many more to be used in encryption srcipts.It is easy to use and can be implement in any scripts with little or no knowledge of Cryptography.

**It is still in devolopment**

# Algoritms include:

Till now I am able include only a handfull of cryptograhic algoritms and **looking forward to add more**.The algorithms included in PyCrypt package :
* Reverse Cipher
* Caeser Cipher
* ROT13 Cipher
* XOR Cipher
* Affine Cipher
* Viginere Cipher

# Installation

From Pypi:

Make sure you're using `python3` and have `pip` installed and enabled. On the command line, simply run:

`pip install pycrypt_dev`

And From GitHub Repo:

clone the repository

`git clone https://github.com/ayanbag/pycrypt.git`

Navigate into the project directory

`cd pycrypt`

Install pydl and its dependencies

`python setup.py install`


# Tutorials

To use **PyCrypt** in your programs, you have to import it : 

`import py.pycrypt`


* Reverse Cipher:

`py.pycrypt.reverse.cipher(message)`

where, message -> It is a set of characters or strings which you want to encrypt.

**NOTE**:

To decrypt the current cipher text which is encrypted with Reverse Cipher,

~~~~
from pycrypt import reverse_cipher
cipher_text="nayA'
print(reverse_cipher(cipher_text))
~~~~
Output : Ayan

* Caeser Cipher:

`py.pycrypt.caesar_cipher(message,encode=False,decode=False)`

where, message ->(string) It is a set of characters or strings which you want to encrypt or decrypt.

encode ->(Boolean) Set *True* if you want to encrypt the current message.By default it is *False*.

decode ->(Boolean) Set *True* if you want to decrypt the current cipher text.By default it is *False*.

* ROT13 Cipher:

`py.pycrypt.rot13_cipher(message)`

where, message ->(string) It is a set of characters or strings which you want to encrypt.

**NOTE**:

To decrypt the current cipher text which is encrypted with ROT13 Cipher,

~~~~
from py.pycrypt import rot13_cipher
cipher_text="nlna'
print(rot13_cipher(cipher_text))
~~~~
Output : ayan

* XOR Cipher:

`py.pycrypt.xor_cipher(message,key)`

where, message ->(string) It is a set of characters or strings which you want to encrypt.

key ->(string) Used to encrypt message.

**NOTE**:

To decrypt the current cipher text which is encrypted with XOR Algoritms,

~~~~
from py.pycrypt import xor_cipher
cipher_text="SHRZ'
print(xor_cipher(cipher_text))
~~~~
Output : ayan

* Affine Cipher:

`py.pycrypt.affine_cipher(message,encode=False,decode=False)`

where, message ->(string) It is a set of characters or strings which you want to encrypt or decrypt.

encode ->(Boolean) Set *True* if you want to encrypt the current message.By default it is *False*.

decode ->(Boolean) Set *True* if you want to decrypt the current cipher text.By default it is *False*.

* Viginere Cipher:

`py.pycrypt.viginere_cipher(message,keyword='crypto',decencode=False,decode=False)`

where, message ->(string) It is a set of characters or strings which you want to encrypt or decrypt.

keyword ->(string) Used to encrypt or decrypt message as key to the lock.

encode ->(Boolean) Set *True* if you want to encrypt the current message.By default it is *False*.

decode ->(Boolean) Set *True* if you want to decrypt the current cipher text.By default it is *False*.

# PyCrypt CLI

PyCrypt comes with a interctive Help CLI. To activate the PyCrypt Help CLI , on the command line, simply run:

`$ pycrypt`

**or**

`$ pycrypt [Funtion_Name]`