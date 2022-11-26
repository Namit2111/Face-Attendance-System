import face_recognition as fr
import cv2
import numpy as np
import csv
import os
import time
import pickle
import Data_Changer as D


#load encoded images 
with open("Resource\\data.pickle",'rb')as f:
    face_known,face_enco_done = pickle.load(f)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)#
        
face_loca = []
face_enco = []
face_name =[]

#to read  video and capture attendance
while True:
    _,frame = cap.read()
    #small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy = 0.25)
    rgb_frame = frame#small_frame#[:,:,::-1]
    if True:
        face_loca = fr.face_locations(rgb_frame)
        face_enco = fr.face_encodings(rgb_frame,face_loca)
        face_name = []
        for face_enc in face_enco:
            matches = fr.compare_faces(face_enco_done,face_enc)
            name = "Unknown_Unknown"
            face_distance = fr.face_distance(face_enco_done,face_enc)
            best_match = np.argmin(face_distance)
            
            if matches[best_match]:
                name = face_known[best_match]
            face_name.append(name)
            D.write(name)
# to add a box on the detected face        
##        for (top, right, bottom, left), name in zip(face_loca, face_name):
##            # Draw a box around the face
##            cv2.rectangle(frame, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)
##
##            # Draw a label with a name below the face
##            cv2.rectangle(frame, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
##            font = cv2.FONT_HERSHEY_DUPLEX
##            cv2.putText(frame, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
        cv2.imshow("a",frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

                
