#816003952-Teneil Rodriguez (python 2.7)

import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto import Random

import socket
clientPort= 1345
clientSocket= socket.socket()
clientHost=socket.gethostname()
clientSocket.connect((clientHost, clientPort))

#caesar encription
def caesar_encript (msg, key):
    
    letters="abcdefghijklmnopqrstuvwxyz"
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc=""
    for sym in msg:
        if sym in letters:
            num= letters.find(sym)
            num= num+key
            
            if num >=len(letters):
                num= num-len(letters)
            elif num < 0:
                num=num+len(letters)
            enc=enc+ letters[num]
        elif sym in LETTERS:
            num= LETTERS.find(sym)
            num= num+key
            
            if num >=len(LETTERS):
                num= num-len(LETTERS)
            elif num < 0:
                num=num+len(LETTERS)
            enc=enc+ LETTERS[num]
        else:
            enc=enc+sym
    return enc




#create rsa private key

prikey=RSA.generate(1024)
#print(prikey)
iv = Random.new().read(DES.block_size)

#create rsa public key

pubkey=prikey.publickey()
#print(pubkey)

#create des key
key='password'

secretMessage=DES.new(key, DES.MODE_CFB, iv)
#print(secretMessage)
#encrypt private key with des key

encPrikey=secretMessage.encrypt(prikey.exportKey(format='PEM'))
#print(encPrikey)

#save encrypted pirvate to file 
out_file=open("privatekey.dat","w")
out_file.write(encPrikey)
out_file.close()

#save public key to file
out_pubkey=open("publickey.dat","w")
out_pubkey.write(pubkey.exportKey(format='PEM'))
out_pubkey.close()  


msg=""
ans=""

#encrypt message to trump
in_file=open("NoWar.dat","r")
lines=in_file.readlines()

length=len(lines)

for list in lines:
    print(list)
   
    msg = pubkey.encrypt(list,32)
    ans+= "".join(msg)
print("-----Message encripted-------")
print(ans)
in_file.close()

#Diffie Hellman
sharedPrime = 23    #p
sharedBase = 13   #b   
secret = 8     #s

# session key A = b^s mod p
Skey = (sharedBase**secret) % sharedPrime

#using caeser encription
encMessage=caesar_encript(ans,Skey)
encDES=caesar_encript(key,Skey)
encPrimKey=caesar_encript(encPrikey,Skey)




#sending encripted data
clientSocket.send(encMessage)
clientSocket.send(encDES)
clientSocket.send(iv)
clientSocket.send(encPrimKey)










