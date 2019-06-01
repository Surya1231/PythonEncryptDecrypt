from tkinter import *
import os
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)

while (True):
    k = input("Enter the operation you want to perform \n1.Encryption\n2.Decryption\n")
    if(k=='1'):
        key = input("Enter Your Secret key\n")
        s = input("Enter the string to be encrypted\n")
        os.system('cls')
        print("Your Encrypter String : \n", encode(key,s))

    else:
        key = input("Enter Your Secret key\n")
        s = input("Enter the string to be decrypted\n")
        print("Your Decrypter String : ", decode(key,s))
