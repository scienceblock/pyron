import csv
from datetime import date
import time
from shutil import copyfile


def encrypt():
    global secretCode
    message = input("t/>> ")

    characters = "1234!£$%^&*()567890QWERT-YUIOPASDFGHJKLZXC=VBNMabcdefghijklmnopqrstuvwxyz.!? "
    encryption = "zyxwvut-srqp!onmlkjihg12345=6789fed£cba?.!MNBVCXZ0A$%SDFGHJKLPOI^&*()UYTREQW¦"

    secretCode = ""

    for letter in message:
            index = characters.index(letter)
            secretCode = secretCode + encryption[index]

    #print( secretCode )





def readmodual():
    try:
        with open(input('d/>>')+'.pyron','r') as modualfile:
            decryption = "1234!£$%^&*()567890QWERT-YUIOPASDFGHJKLZXC=VBNMabcdefghijklmnopqrstuvwxyz.!? "
            characters = "zyxwvut-srqp!onmlkjihg12345=6789fed£cba?.!MNBVCXZ0A$%SDFGHJKLPOI^&*()UYTREQW¦"
            decryptcode = ""
            for row in modualfile:
                #print(row)
                for letter in row:
                    index = characters.index(letter)
                    decryptcode = decryptcode + decryption[index]
                print(decryptcode)
            print('-END-')
    except:
        print('Erron: file not found')

def writemodual():
    try:
        with open(input('d/>>')+'.pyron','w') as modualfile:
            for row in secretCode:
                modualfile.write(row)
        print('-WRITTEN-')
    except:
        print('Erron: file cannot be written')
            

print('*'*60)
print(' '*28,'log')
print('*'*60)

x = 1

while x == 1:
    menop = input('''
1 - writefile
2 - readfile
3 - help
4 - exit
m/>>''')
    if menop == '1':
        encrypt()
        writemodual()
    elif menop == '2':
        readmodual()
    elif menop == '3':
        print('''
Iteration - pyron x
Version - 1.0.1
Pep version - 1.0.0''')
    elif menop == '4':
        x = 0
    else:
        print('invalid option')
        

    

#import tkinter
#top = tkinter.Tk()

#top.mainloop()
