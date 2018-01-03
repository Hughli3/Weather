import cv2
import os
import configparser
import numpy as np

os.chdir("C:/Users/hughli/OneDrive/henan/data")
os.chdir("/Users/hughli/Pictures/video/test")

cf = configparser.ConfigParser()
cf.read("capture_setting.ini")

def information():
    address_in = cf.get("address", "address_in")
    address_out = cf.get("db", "address_out")

    return address_in,address_out

os.chdir(address_in)

vc = cv2.VideoCapture('/Users/hughli/Pictures/video/test鹤壁_鹤壁_1_20170902080000_20170902090000_1.avi') #读入视频文件
c=1



if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
else:
    rval = False

timeF = 1000  #视频帧计数间隔频率

cv.open(0)

while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)

rval
vc.release()


vc = cv2.VideoCapture('test.avi') #读入视频文件
c=1
if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
else:
    rval = False
print(rval)
timeF = 1000  #视频帧计数间隔频率
while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()


-----------------------------------
videoCapture = cv2.VideoCapture('output.avi')
#读取avi额格式文件
fps = VideoCapture.get(cv2.CAP_PROP_FPS)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter(
'video.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
fps, size)

success, frame = videoCapture.read()

while success :
    videoWriter.write(frame)
    success, frame = videoCapture.read()

--------------------------------------
cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv.VideoWriter(
'video.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
    cameraCapture.release()
