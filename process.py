from operator import index
from time import pthread_getcpuclockid
import cv2
import os

name=""
path = "/home/zst/Documents/cv/123"
images = []


for filename in os.listdir(path):
    images.append(os.path.join(path, filename))

huojia1 = []
for image in images:
    image_name = image.split('/')[-1]
    if image_name.startswith(name):
        huojia1.append(image)

# 对货架1的图片每10个进行处理
for i in range(0, len(huojia1), 10):
    # 对10张图片赋给不同的对比度和亮度
    for j in range(10):
        img = cv2.imread(huojia1[i + j])
        cv2.convertScaleAbs(img, img, 0.8, 0)
        cv2.imwrite(f"{huojia1[i + j]}", img)
        
