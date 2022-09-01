import face_recognition as fr
import cv2
import numpy as np
import csv
import os
import time


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)#

w = 1
t = time.localtime()
ct = time.strftime("%H:%M:%S", t)
student=[]


##f = open('C:/Users/NAMIT/Desktop/New folder/my-app/src/Dataforface.js','w')
##f.write("const C = [\n"  )
##f.write("\n]; export default C")
##f.close()
r = "2121382"
def write(name):
    print(name)
    
        
        
    if name not in student:
        student.append(name)
        f = open('C:/Users/NAMIT/Desktop/New folder/my-app/src/Dataforface.js','w')     
        f.write("const C = [\n"  )
        student.sort()
        for i in student:
            if i == "Unknown":
                continue
            
           
        
        
        
       
            f.write("\n{ Name : " + '"'+i + '"'+", RollNO : " + r + "},")
        f.write("\n]; export default C")

        f.close()
        
        
    
        
    
    
    

def img_enc():
    encoded={}
    img_list = os.listdir("face_rec/faces")
    for f in img_list:
        face = fr.load_image_file("face_rec/faces/"+f)
        face_enc = fr.face_encodings(face)[0]
        encoded[f.split(".")[0]] = face_enc
    return list(encoded.keys()),list(encoded.values())
face_known,face_enco_done= img_enc()


face_loca = []
face_enco = []
face_name =[]
##now = datetime.now()
##current_date = now.strftime("%Y-%m-%d")


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
            name = "Unknown"
            face_distance = fr.face_distance(face_enco_done,face_enc)
            best_match = np.argmin(face_distance)
            
            if matches[best_match]:
                name = face_known[best_match]
            face_name.append(name)
            write(name)
        
##        for (top, right, bottom, left), name in zip(face_loca, face_name):
##            # Draw a box around the face
##            cv2.rectangle(frame, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)
##
##            # Draw a label with a name below the face
##            cv2.rectangle(frame, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
##            font = cv2.FONT_HERSHEY_DUPLEX
##            cv2.putText(frame, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
##            
##
           
            
        
        cv2.imshow("a",frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        
        
        break
cap.release()
cv2.destroyAllWindows()

                
