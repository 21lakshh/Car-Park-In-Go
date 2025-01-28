import cv2
from PIL import Image
import matplotlib.pyplot as plt
import pickle
import os 

working_dir = os.path.dirname(os.path.abspath(__file__))
# directory where the script is located
try:
    with open(f"{working_dir}/car_positions.pkl", 'rb') as f:
        position_list = pickle.load(f)
except:
    position_list = []


width = 110 # cropped image dimensions 
height = 45

save_dir = f"{working_dir}/cropped_images1"
# directory where cropped images will be saved

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def save_cropped_img(img, pos, index):
    cropped_img = img[pos[1]:pos[1]+height, pos[0]:pos[0]+width]
    save_path = os.path.join(save_dir, f'roi_{index}.png')
    cv2.imwrite(save_path, cropped_img)
    print(f'saved cropped image: {save_path}')
 # saving a cropped image   

def mouseclick(events,x,y,flags,param):
    if events == cv2.EVENT_LBUTTONDOWN:
        position_list.append((x,y))
        save_cropped_img(cv2.resize(cv2.imread(f"{working_dir}/parkinglot.png"), (1280, 720)), (x, y), len(position_list))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(position_list):
            if pos[0] < x < pos[0]+width and pos[1] < y < pos[1]+height:
                del position_list[i]
                break
    with open(f"{working_dir}/car_positions.pkl", 'wb') as f:
        pickle.dump(position_list, f)

while True: 

    img = cv2.imread(f"{working_dir}/parkinglot.png")
    img = cv2.resize(img, (1280, 720))
    for pos in position_list:
        cv2.rectangle(img, pos, (pos[0]+width,pos[1]+height), (255, 0, 255), 2)
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image', mouseclick)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

