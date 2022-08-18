import cv2
cap = cv2.VideoCapture(0)
index=0
for i in range(index,index+10):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)
    cap.set(cv2.CAP_PROP_CONTRAST, 20)
    cap.set(cv2.CAP_PROP_EXPOSURE, -20)
    (ret, frame) = cap.read()
    cv2.imwrite('./jpeg/shujuji'+str(i+1).zfill(4)+'.jpg',frame)
    cv2.waitKey(10)
