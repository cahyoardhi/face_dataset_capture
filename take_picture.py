from cv2 import cv2
import os
import time

DIR_NAME = 'dataset/'
_help = "1.manual\n2.auto"


def cameraCheck():
    camera = cv2.VideoCapture(1)
    if camera.isOpened == False:
        camera = cv2.VideoCapture(0)
    return camera


def modeMethod():
    print(_help)
    method = int(input('mode : '))
    return method


def saveFileDir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def takeData(mode, camera):
    if mode == 1:
        try:
            count = 1
            while True:
                ret, frame = camera.read()
                if ret == False:
                    continue
                cv2.imshow("frame", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('s'):
                    cv2.imwrite('dataset/'+str(count)+".jpg", frame)
                    count += 1
                if key == ord('q'):
                    camera.release()
                    cv2.destroyAllWindows()
                    break

        except KeyboardInterrupt:
            camera.release()
            cv2.destroyAllWindows()
    else:
        try:
            _time = time.time()
            count = 1
            while True:
                ret, frame = camera.read()
                if ret == False:
                    continue
                cv2.imshow("frame", frame)
                time_capture = time.time() - _time
                key = cv2.waitKey(1) & 0xFF
                if time_capture >= 10:
                    cv2.imwrite('dataset/'+str(count)+".jpg", frame)
                    print("picture has been saved")
                    _time = time.time()
                    count += 1
                if key == ord('q'):
                    camera.release()
                    cv2.destroyAllWindows()
                    break
                if count >= 1000:
                    camera.release()
                    cv2.destroyAllWindows()
                    break
        except KeyboardInterrupt:
            camera.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = cameraCheck()
    saveFileDir(DIR_NAME)
    mode = modeMethod()
    takeData(mode, camera)
    exit()
