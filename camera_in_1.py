import cv2

cap = cv2.VideoCapture()    # == cap = cv2.VideoCapture(0)
cap.open(0)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

print('Frame width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)    # edge detection

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()