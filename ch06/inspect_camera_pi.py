#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

if __name__ == '__main__':
    # parse options
    parser = argparse.ArgumentParser(description='tf-pi.')
    parser.add_argument('-m', '--model', default='./my_model_aug.h5')
    parser.add_argument('-l', '--labels', default='./labels.txt')

    args = parser.parse_args()

    camera = PiCamera()
    camera.resolution = (640, 480)

    labels = []
    with open(args.labels, 'r') as f:
        for line in f:
            labels.append(line.rstrip())
    print(labels)

    model_pred = tf.keras.models.load_model(args.model)
    # model_pred.summary()

    max_count = 0
    count = 0
    stream = PiRGBArray(camera)
    while True:
        camera.capture(stream, 'bgr', use_video_port=True)
        key = cv2.waitKey(1)
        if key == 27:  # when ESC key is pressed break
            break

        count += 1
        if count > max_count:
            X = []
            img_org = stream.array
            img = cv2.resize(img_org, (64, 64))
            img = img_to_array(img)
            X.append(img)
            X = np.asarray(X)
            X = X/255.0
            start = time.time()
            preds = model_pred.predict(X)
            elapsed_time = time.time() - start

            pred_label = ''

            label_num = 0
            tmp_max_pred = 0
            print(preds)
            for i in preds[0]:
                if i > tmp_max_pred:
                    pred_label = labels[label_num]
                    tmp_max_pred = i
                label_num += 1

            # Put speed
            speed_info = '%s: %f' % ('speed=', elapsed_time)
            # print(speed_info)
            cv2.putText(img_org, speed_info, (10, 50),
                  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            # Put label
            cv2.putText(img_org, pred_label, (10, 100),
                  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imshow('tf-pi inspector', img_org)
            count = 0
        stream.seek(0)
        stream.truncate()

    camera.close()
    cv2.destroyAllWindows()
