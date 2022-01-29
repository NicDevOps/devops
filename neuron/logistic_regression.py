import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy

ROWS = 64
COLS = 64
CHANNELS = 3

train_images = [TRAIN_DIR+i for i in os.listdir(TRAIN_DIR)]
test_images = [TEST_DIR+i for i in os.listdir(TEST_DIR)]

def read_image(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    return cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)

def prepare_data(image):
    m = len(image)
    X = np.zeros((m, ROWS, COLS, CHANNELS), dtype=uint8)
    y = np.zeros(1, m)
    for i, image_file in enumerate(image):
        X[i,:] = read_image(image_file)
        if 'dog' in image_file.lower():
            y[0, i] = 1
        elif 'cat' in image_file.lower():
            y[0, i] = 0

    return X, y

train_set_x, train_set_y = prepare_data(train_images)
test_set_x, test_set_y = prepare_data(test_images)

train_set_x_flattern = train_set_x.reshape(train_set_x.shape[0], ROWS * COLS * CHANNELS).T
test_set_x_flattern = test_set_x.reshape(test_set_x.shape[0], -1).T

print(train_set_x.shape)
print(train_set_x_flattern.shape)
print(train_set_y.shape)
print(test_set_x.shape)
print(test_set_x_flattern)
print(test_set_y)

