import numpy as np
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    if cv2.waitKey(10) > 0: 
        break

    ret, frame = capture.read()

    cv2.putText(frame,'test',(0,25), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
    cv2.imshow("camera test", frame)



import tensorflow.keras
import numpy as np
import cv2

model_filename ='C:\\AISpace\\keras_model.h5'
model = tensorflow.keras.models.load_model(model_filename)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


def preprocessing(frame):
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

    return frame_reshaped


def predict(frame):
    prediction = model.predict(frame)
    return prediction

while True:
    ret, frame = capture.read()

    if cv2.waitKey(100) > 0: 
        break

    preprocessed = preprocessing(frame)
    prediction = predict(preprocessed)

    if (prediction[0,0] < prediction[0,1]):
        print('case1')
        cv2.putText(frame, 'case1', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
    else:
        cv2.putText(frame, 'case2', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
        print('case2')

    cv2.imshow("VideoFrame", frame)
