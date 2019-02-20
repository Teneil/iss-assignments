#816003952-Teneil Rodriguez (python 3.6)
import socket 

serverPort= 1345
serverSocket= socket.socket()
serverHost=socket.gethostname()
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
connectionSocket, addr=serverSocket.accept()
out=open("Trump.dat","w")
data=connectionSocket.recv(1024)
out.write(data.decode())





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




def rail_decript(msg, key1,key2):
    enc = ""
    ans = ""
    matrix = [["" for x in range(len(msg))] for y in range(key1)]
    result=[[0 for y in range(len(matrix))] for x in range ( len(matrix[0]))]
    idx = 0
    k=1
    matlen = len(matrix)
    for sel in range(0, matlen):
        row=0
        
        for col in range (0, len(matrix[row])):
            if row == sel:
                matrix[row][col]+= msg[idx]
                idx +=1
                
            if row + k < 0 or row + k >= len(matrix):
                k = k *(-1)
            row += k
                
    for i in range ( len (matrix)):
        for j in range (len (matrix[0])):
            result [j][i]=matrix[i][j]
    for list in result:
        enc += "".join(list)
    ans=caesar_decript(enc,key2)
    return ans
















in_file=open("Trump.dat","r")
encrypt=True
lines=in_file.readlines()
length=len(lines)




while encrypt== True:
    key1 = input ("please enter key 1: ")
    key1 = int(key1)
    key2 = input ("please enter key 2: ")
    key2 = int(key2)
    msg=""
    ans=""


    for list in lines:
       
        msg = rail_decript(list.rstrip(),key1,key2)
        ans+= "".join(msg+"\n")
   
    res=ans.count("Trump")
    
    if res>0:
        encrypt=False
print("letter was decripted \n")
print(ans)
in_file.close()
out.close()
connectionSocket.close()
