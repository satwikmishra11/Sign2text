import os
import time
import uuid
import cv2

# Define the folder to save the images
IMAGES_PATH = 'images'

if not os.path.exists(IMAGES_PATH):
    os.makedirs(IMAGES_PATH)

# Define the labels for the images to be collected

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'del', 'space']

# Number of images to be collected for each label
number_imgs = 100

# Define the camera to be used
cap = cv2.VideoCapture(0)

# Define the size of the window
cap.set(3, 640)

# Collect the images for each label

for label in labels:
    if not os.path.exists(os.path.join(IMAGES_PATH, label)):
        os.makedirs(os.path.join(IMAGES_PATH, label))
    print('Collecting images for {}'.format(label))
    time.sleep(10)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()