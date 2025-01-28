import cv2
import numpy as np
import pickle
import os
import tensorflow as tf
from PIL import Image

working_dir = os.path.dirname(os.path.abspath(__file__))

model_path = f"{working_dir}/model_final.h5"
model = tf.keras.models.load_model(model_path)

class_names = {0: 'Vacant', 1: 'Occupied'}

video = cv2.VideoCapture(f"{working_dir}/carPark.mp4")

with open(f"{working_dir}/car_positions.pkl", 'rb') as f:
    position_list = pickle.load(f)

width = 110
height = 45

def checkingCarParking(img):
    imgCrops = []
    spaceCounter = 0 # counts number of vacant spots 
    for pos in position_list:
        x, y = pos # position of the cropped image
        cropped_img = img[y:y+height, x:x+width]
        imgResized = cv2.resize(cropped_img, (48,48))
        imgNormalized = imgResized/255.0
        imgCrops.append(imgNormalized)
    imgCrops = np.array(imgCrops)
    predictions = model.predict(imgCrops)

    for i, pos in enumerate(position_list):
        x, y = pos
        predicted_class_index = np.argmax(predictions[i])
        predicted_class_name = class_names[predicted_class_index]
        if predicted_class_name == 'Vacant':
            color = (0,255,0)
            thickness = 5
            spaceCounter +=1
            textColor = (0,0,0)
        else:
            color = (0,0,255)
            thickness = 2
            textColor = (255,255,255)

        cv2.rectangle(image, pos, (pos[0]+width, pos[1]+height), (255,0,255), thickness)
        font_scale = 0.5
        text_thickness = 1
        
        textSize = cv2.getTextSize(predicted_class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_thickness)[0]
        textX = x
        textY = y + height - 5
        cv2.rectangle(img, (textX, textY - textSize[1] - 5), (textX + textSize[0] + 6, textY + 2), color, -1)
        cv2.putText(img, predicted_class_name, (textX + 3, textY - 3), cv2.FONT_HERSHEY_SIMPLEX, font_scale, textColor, text_thickness)
    cv2.putText(image, f'Space Count: {spaceCounter}', (100, 50), (cv2.FONT_HERSHEY_SIMPLEX), 1, textColor, 2)


while True:
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, image = video.read()
    image = cv2.resize(image, (1280, 720))
    if not ret:
        break
    checkingCarParking(image)
    cv2.imshow('Video', image)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()