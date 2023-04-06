# Attendance-using-face-recognition
Train a ‘Face-recognition’ model using OpenCV 
In this project we are going to train a ‘Face-recognition’ model using OpenCV and then we are going to save the images of the students and if the camera recognizes the student it marks the attendance of the student and save the date and time in an excel file. The deployment of this model is using stream-lit. The project can be broadly classified into :-
1.) Face Recognition
2.) Generate Image Dataset from live video 
3.) Train model with the Image Dataset
4.) Face Recognition with name
5.) Deployment of model using Stream-Lit
6.) Saving the student data in the Excel file


                        Objective :
The basic objective of this project is to ‘Generate-Train-Recognize.’ The user is going to click on the link and I site will pop up. Camera will open and then our model will try to recognize the user face, once it recognizes it, it will try to compare it and then if the user is in the class list then It will display the name of that face under the face and then it will mark the attendance of that user in the attendance.csv sheet and the time and date also at which the attendance is marked is saved.

                         Working:

In this project I have used ‘Face Recognition’ module . I installed the module using pip install face_recognition command by activating my environment.
 
First  I imported some important libraries like numpy,pandas,os,cv2 and datetime. 
 
Then I added some images for training purpose in my project.
 
After that I created a function named as ‘find encodings’ which using the ‘face recognition’ module find the encodings of all the training images. 
 
After finding the encodings I saved those encodings in a list. 
After that I created a function which marks the attendance by reading the name under the face and also saving the date and time at which the attendance is marked. 
 
After that using CV2 I used my laptop’s camera as a test camera. Then I allowed my model to compare face encodings on the camera and the encodings of the trained images. Once it compares all the images with the face then the image with most close match is chosen. The name of that face is displayed below the face, and a square outlining is also done to mark the locations of the face.
 
I have deployed my model using flask, which is a web app deployer for ML models. I used basic CSS and HTML for my site and as soon as the face will be recognized on the site, the attendance will be marked in the Attendance.csv file.  
 
 
 
 

                             Tools and Resources
These are the tools that came in use when I was creating this project:
1 )VSCode-Code Editor
2)Python – 3.9.16 (version)
3)Cv2 Library
4)Face_Recognition library

                              Conclusion
It was an experience of great learning and exploration in conceptualizing and building this project.  I have been doing machine learning and deep learning but I am still a beginner and this was my first project toward OpenCV and I enjoyed it a lot and gained new experience.
