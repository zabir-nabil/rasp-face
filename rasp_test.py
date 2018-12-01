import picamera
from time import sleep
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
import keras
import numpy as np
from PIL import Image
from keras.models import load_model

# confidence check with same class for continuous 3 frames
v1 = 0, v2 = 0, v3 = 0
model1 = load_model('rasp-face1.h5')
print('--------------------------------------------------\n')
xx = input('The program will run for X frames, Enter X (Example 100): ')
xx = int(xx)
for fr in range(xx):

  camera = picamera.PiCamera()

  camera.resolution = (512,512)

  camera.start_preview()

  sleep(2)

  camera.capture('cur_frame.jpg')

  camera.stop_preview()

  x = 'cur_frame.jpg'
  im = Image.open(x2)
  im = im.resize((224,224), Image.ANTIALIAS)
  a = np.array(im, dtype='float32')
  a = np.reshape(a, (1,224,224,3))
  a = a/255.
  pr = model1.predict_classes(a)
  pr = pr[0]
  
  v1 = v2
  v2 = v3
  v3 = pr
  
  if(v1==1 and v2==1 and v2==2):
    print('Imran (Class 1) seen on camera')
    print('\n')
  elif(v1==1 and v2==1 and v2==2):
    print('Sadman (Class 2)seen on camera')
    print('\n')
  else:
    print('Background or Unknown face!')
    print('\n')