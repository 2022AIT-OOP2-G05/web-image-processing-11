import numpy as np
import cv2


def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def face_mosaic(image_name : str):


    image = cv2.imread(image_name)

    face_cascade_path = '/usr/local/opt/opencv/share/'\
                    'OpenCV/haarcascades/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image_gray)

    for x, y, w, h in faces:
        
        dst_face = mosaic_area(image, x, y, w, h)
    


    cv2.imwrite('mosaic.png', dst_face)

    




    





            
    
    




if __name__ == "__main__":
    face_mosaic('uchitane_near.png')
    





