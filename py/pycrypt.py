import pyperclip
import sys
#Usage
usage = "pycrypt [option]"
#Version
Version= "pycrypt_dev/0.1.dev1"
#=============Reverse Cipher================

def reverse_cipher(message):

    cipher=''
    i = len(message) - 1
    while i >= 0:
        cipher = cipher + message[i]
        i = i - 1
    return cipher

#=============Caeser Cipher================

def caeser_cipher(message,shift=7,encode=False,decode=False):
    cipher=""
    if encode:
        for i in range(len(message)):
          char = message[i]
        if (char.isupper()):
            cipher += chr((ord(char) + shift-65) % 26 + 65)
        else:
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
        return cipher
    elif decode:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decp_lst=[]
        for key in range(len(LETTERS)):
            decipher = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    decipher = decipher + LETTERS[num]
                else:
                    decipher = decipher + symbol
            decp_lst.append(decipher)
        return decp_lst
            
#=============ROT13 Cipher================

def rot13_cipher(message):
    cipher = ""
    for v in message:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        cipher += chr(c)
    return cipher

#=============XOR Cipher================

def xor_cipher(message,key='2134'):
    cipher = ""
    for i in range(len(message)):
        current = message[i]
        current_key = key[i%len(key)]
        cipher += chr(ord(current) ^ ord(current_key))
    return cipher

#=============Affine Cipher================

K1=7
K2=86
KI=32
dot=128

def encryptChar(char):
    return chr((K1 * ord(char) + K2) % dot)

def decryptChar(char):
      return chr(KI * (ord(char) - K2) % dot)

def affine_cipher(message,encode=False,decode=False):
    if encode:
        return "".join(map(encryptChar, message))
    if decode:
        return "".join(map(decryptChar, message))


#=============Viginere Cipher================

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def viginere_cipher(message, keyword="crypto",encode=False,decode=False): 
    key=generateKey(message, keyword)
    if encode:
        cipher_text = [] 
        for i in range(len(message)): 
            x = (ord(message[i]) + 
                ord(key[i])) % 26
            x += ord('A') 
            cipher_text.append(chr(x)) 
        return("" . join(cipher_text)) 
      
    if decode: 
        orig_text = [] 
        for i in range(len(message)): 
            x = (ord(message[i]) - 
                ord(key[i]) + 26) % 26
            x += ord('A') 
            orig_text.append(chr(x)) 
        return("" . join(orig_text)) 

#============Help Console==================

def load():
    help_cmd={'RevCp': 'To view Synatx of Reverse Cipher','CaeCp':'To view Synatx of Caeser Cipher',
    'ROTCp':'To view Synatx of ROT13 Cipher','XORCp':'To view Synatx of XOR Cipher',
    'AffCp':'To view Synatx of Affine Cipher','VigCp':'To view Synatx of Vignere Cipher'}
    print("CLI to interact with PyCrypt help")
    print("")
    print("Version")
    print("  "+Version)
    print("")
    print("Usage")
    print("  "+usage)
    print("")
    print("Command")
    for x in help_cmd:
        print(" %s    %s"%(x,help_cmd[x]))

def main():
    view_cmd={'RevCp': 'reverse_cipher(message)','CaeCp':'caesar_cipher(message,encode=False,decode=False)',
    'ROTCp':'rot13_cipher(message)','XORCp':'xor_cipher(message,key)',
    'AffCp':'affine_cipher(message,encode=False,decode=False)','VigCp':'viginere_cipher(message,keyword="crypto",decencode=False,decode=False)'}
    if len(sys.argv)>1:
        command=sys.argv[1]
        print("")
        print("Syntax: ")
        print(" from py.pycrypt import *")
        print(" %s"%(view_cmd[command]))
    else:
        load()

