#816003952-Teneil Rodriguez (python 3.6)
import socket 
clientPort= 1345
clientSocket= socket.socket()
clientHost=socket.gethostname()
clientSocket.connect((clientHost, clientPort))





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


def rail_encrypt(msg, key1,key2 ):
    enc = ""
    ans=""
    matrix = [["" for x in range(len(msg))] for y in range(key1)]
    matlen = len(matrix)
 
    row = 0
    col = 0
    k=1
    

    for c in msg:
        
        matrix[ row ][ col ] = c
        col = col + 1
        if row + k < 0 or row + k >= len(matrix):
            k = k *(-1)
        
        
        row += k
    
        
        
    for list in matrix:
        enc += "".join(list)
 
    ans=caesar_encript(enc,key2)
    return ans








key1 = input ("please enter key 1: ")
key1 = int(key1)
key2 = input ("please enter key 2: ")
key2 = int(key2)
msg=""
ans=""
in_file=open("NoWar.dat","r")
lines=in_file.readlines()

length=len(lines)

for list in lines:
   
    msg = rail_encrypt(list.rstrip(),key1,key2)
    
    ans+= "".join(msg+"\n")
print(ans)
out_file=open("Trump.dat","w")
out_file.write(ans)

in_file.close()

clientSocket.send(bytes(ans,"utf-8"))

out_file.close()


clientSocket.close()
    

