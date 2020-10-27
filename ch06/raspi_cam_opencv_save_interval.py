# coding: utf-8
# raspi cam lapse
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import datetime
import time

camera = PiCamera()
camera.resolution = (640, 480)

count_max = 10

if __name__ == '__main__':
    count = 0

    stream = PiRGBArray(camera)

    try:
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            img = stream.array

            count += 1
            if count > count_max:
                now = datetime.datetime.now()
                filename = './log_' + now.strftime('%Y%m%d_%H%M%S') + '.jpg'
                print(filename)
                cv2.imwrite(filename, img)
                count = 0

            stream.seek(0)
            stream.truncate()
            time.sleep(0.1)

    except KeyboardInterrupt:
        print('Ctrl+C interrupted')
