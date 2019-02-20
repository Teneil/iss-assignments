#816003952-Teneil Rodriguez part1 (python 3.6)


def encript(msg, key ):
    enc = ""
    
    matrix = [["" for x in range(len(msg))] for y in range(key)]
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
 
    return enc

def decript(msg, key):
    enc = ""
    
    matrix = [["" for x in range(len(msg))] for y in range(key)]
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
                
    for i in range ( len(matrix)):
        for j in range (len (matrix[0])):
            result [j][i]=matrix[i][j]
    for list in result:
        enc += "".join(list)
    return enc

def caesar (msg, key,m):
    
    letters="abcdefghijklmnopqrstuvwxyz"
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc=""
    for sym in msg:
        if sym in letters:
            num= letters.find(sym)
            if m=='e':
                num= num+key
            elif m=='d':
                num = num-key
            if num >=len(letters):
                num= num-len(letters)
            elif num < 0:
                num=num+len(letters)
            enc=enc+ letters[num]
        elif sym in LETTERS:
            num= LETTERS.find(sym)
            if m=='e':
                num= num+key
            elif m=='d':
                num = num-key
            if num >=len(LETTERS):
                num= num-len(LETTERS)
            elif num < 0:
                num=num+len(LETTERS)
            enc=enc+ LETTERS[num]
        else:
            enc=enc+sym
    return enc
    
            





def main():
    
    msg = input("please enter message: ")
    mode = input("enter 'e' to encrypt or 'd' to decrypt: ")
    key1= input ("please enter key 1: ")
    key1 = int(key1)
    key2= input ("please enter key 2: ")
    key2 = int(key2)
    ans=''
    if mode == 'e':
        enc = encript( msg, key1 )
        ans=caesar(enc,key2,mode)
    if mode == 'd':
        enc= decript(msg, key1)
        ans=caesar(enc,key2,mode)
    print(msg)
    print (ans)

    
main()
