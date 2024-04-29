import cv2
from pyzbar.pyzbar import decode
from time import sleep

IMAGE = "./pic.jpg"

def read_qr_code(image):
    # image = cv2.imread(filepath)
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            print(f"QR Code Data: {data}")
    else:
        print("did not find any QR code")


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    read_qr_code(frame)
    sleep(1)

 