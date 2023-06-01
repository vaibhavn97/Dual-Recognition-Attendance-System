import numpy as np
import cv2
import face_recognition
import os
import time

path = 'Images'
images = []
className = []
myList = os.listdir(path)

for i in myList:
    img = cv2.imread(f"{path}/{i}")
    images.append(img)
    className.append(os.path.splitext(i)[0])

print(className)

def find_encodings(images):
    encodedImages = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodedImages.append(encode)
    return encodedImages

encodedListKnowned = find_encodings(images)




def detectFace():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    while ( int(time.time() - start_time) < 8 ):
        ret, frame = cap.read()
        if ret==True:
            sucess, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            currFacesLoc = face_recognition.face_locations(imgS)
            encodedCurrFrame = face_recognition.face_encodings(imgS, currFacesLoc)

            for encodedFace, faceLoc in zip(encodedCurrFrame, currFacesLoc):
                matches = face_recognition.compare_faces(encodedListKnowned, encodedFace)
                faceDis = face_recognition.face_distance(encodedListKnowned, encodedFace)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = className[matchIndex]
                    print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1 = y1*4
                    y2 = y2*4
                    x1 = x1*4
                    x2 = x2*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
                    cap.release()
                    return name
            cv2.imshow("WebCam", img)
            cv2.waitKey(1)
    return "NFD"
