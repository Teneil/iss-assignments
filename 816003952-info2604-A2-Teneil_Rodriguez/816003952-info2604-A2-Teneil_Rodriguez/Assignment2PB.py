#816003952-Teneil Rodriguez (python 2.7)
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto import Random

import socket 
serverPort= 1345
serverSocket= socket.socket()
serverHost=socket.gethostname()
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)


connectionSocket, addr=serverSocket.accept()

#the sent data from program A
ans=connectionSocket.recv(1024)
key=connectionSocket.recv(1024)
iv=connectionSocket.recv(1024)
encPriKey=connectionSocket.recv(1024)

#caesar decription
def caesar_decript (msg, key):
    
    letters="abcdefghijklmnopqrstuvwxyz"
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc=""
    for sym in msg:
        if sym in letters:
            num= letters.find(sym)
            num = num-key
            if num >=len(letters):
                num= num-len(letters)
            elif num < 0:
                num=num+len(letters)
            enc=enc+ letters[num]
        elif sym in LETTERS:
            num= LETTERS.find(sym)
            
            num = num-key
            if num >=len(LETTERS):
                num= num-len(LETTERS)
            elif num < 0:
                num=num+len(LETTERS)
            enc=enc+ LETTERS[num]
        else:
            enc=enc+sym
    return enc

#Diffie Hellman
sharedPrime = 23    #p
sharedBase = 13   #b   
secret = 8     #s

# session key A = b^s mod p
Skey = (sharedBase**secret) % sharedPrime

#using caeser decription
Message=caesar_decript(ans,Skey)

DESkey=caesar_decript(key,Skey)

PrimKey=caesar_decript(encPriKey,Skey)

secretMessage=DES.new(DESkey, DES.MODE_CFB, iv)

dcrPrikey=secretMessage.decrypt(PrimKey)

privatekey=RSA.importKey(dcrPrikey)
#print(privatekey)

#decription of the message
   
ans = privatekey.decrypt(Message)
    

#printing decripted message
print("------Message decripted-------")
print(ans)
