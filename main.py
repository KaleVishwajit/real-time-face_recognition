
#IMPORT
import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet

# INITIALIZE
facenet = FaceNet()

faces_embeddings = np.load("faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']

encoder = LabelEncoder()
encoder.fit(Y)

haarcascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
model = pickle.load(open("svm_model_160x160.pkl", 'rb'))

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# WHILE LOOP
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haarcascade.detectMultiScale(gray_img, 1.3, 5)

    for x, y, w, h in faces:
        img = rgb_img[y:y+h, x:x+w]
        img = cv.resize(img, (160, 160))
        img = np.expand_dims(img, axis=0)

        try:
            ypred = facenet.embeddings(img)
            face_name = model.predict(ypred)
            final_name = encoder.inverse_transform(face_name)[0]
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
            cv.putText(frame, str(final_name), (x, y - 10), cv.FONT_HERSHEY_SIMPLEX,
                       0.9, (0, 0, 255), 2, cv.LINE_AA)
        except Exception as e:
            print("Prediction error:", e)

    cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


