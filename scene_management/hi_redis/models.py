from django.db import models
from redis import Redis
redis_cli=Redis(host='localhost',port=6379,db=1)

# Create your models here.
redis_cli.set('name','aaaa')
redis_cli.get('name')
print(redis_cli.get('name'))
# import cv2
# #rtsp://用户名:密码@ip地址/Streaming/Channels/2
# url = "rtsp://admin:sspu16119@192.168.1.64/Streaming/Channels/1"
# cap = cv2.VideoCapture(url)
# ret, frame = cap.read()
# print(ret)
# while ret:
#     ret, frame = cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
# cap.release()