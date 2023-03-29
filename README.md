# Face Recognition Attendance System
This is a Python program that uses the face_recognition library and OpenCV to recognize faces in a live video stream and take attendance. It compares the detected face with pre-registered images and labels the recognized face with the registered name.

# Installation
Before running the program, the following Python libraries should be installed:
1. face_recognition
2. opencv-python
3. numpy
4. csv
5. pickle
To install these libraries, run the following command:

# Usage
To run this project, follow the steps below:

1. Clone the repository to your local machine
2. Install the necessary packages using the following command:
```
pip install face_recognition opencv-python numpy csv pickle
```
3. Collect the images of the faces you want to recognize and save them in the Resources/Faces folder.
4. Train the model using the face_train.py script. This will create a data.pickle file containing the encodings of the faces in the Faces folder.
5. Run the main.py script to start the face recognition system.
6. The script captures video from the webcam and recognizes the faces in real-time. The name of the recognized person is displayed on the screen.
7. To exit the program, press 'q' on the keyboard.
Note: This project has been created using Python 3.7, OpenCV 4.5, and face_recognition 1.3.0.

# Integration on a website
This project is supposed to be integrated with website that is created using ReactJS and NodeJS , it helps in viewing which person is present and has its attendace marked.
