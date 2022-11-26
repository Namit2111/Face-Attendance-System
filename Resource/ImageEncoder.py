import face_recognition as fr
import pickle
import os
def img_enc():
    encoded={}
    img_list = os.listdir("faces")
    for f in img_list:

        face = fr.load_image_file("faces\\"+f)
        face_enc = fr.face_encodings(face)[0]
        encoded[f.split(".")[0]] = face_enc
    return list(encoded.keys()),list(encoded.values())
face_known,face_enco_done= img_enc()
with open("data.pickle","wb")as f:
    pickle.dump((face_known,face_enco_done),f)
    

