from flask import Flask,render_template,Response
import cv2
#Importing Important Libraries
import numpy as np
import os
import face_recognition
from datetime import datetime


path='Training_images'
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)

for cl in mylist:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)

def findencodings(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodelistknown=findencodings(images)

def markattendance(name):
    with open('Attendance.csv','r+') as f:
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now=datetime.now()
            dtstring=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')


app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,img=camera.read()
        if not success:
            break
        else:
            
            imgs=cv2.resize(img,(0,0),None,0.25,0.25)
            imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

            faces_curframe=face_recognition.face_locations(imgs)
            encodings_curframe=face_recognition.face_encodings(imgs,faces_curframe)

            for encodeface,faceloc in zip(encodings_curframe,faces_curframe):
                matches=face_recognition.compare_faces(encodelistknown,encodeface)
                facedis=face_recognition.face_distance(encodelistknown,encodeface)

                matchindex=np.argmin(facedis)

                if matches[matchindex]:
                    name=classnames[matchindex].upper()
                    y1,x2,y2,x1=faceloc
                    y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    markattendance(name)
            ret,buffer=cv2.imencode('.jpg',img)
            img=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
