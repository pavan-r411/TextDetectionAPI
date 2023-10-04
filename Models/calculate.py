import easyocr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Image
import cv2

reader = easyocr.Reader(['en'])
IMAGE_PATH = 'C:\\Users\\I569380\\Documents\\VSProj\\DecisionAPI\\Models\\card2.jpg'
result = reader.readtext(IMAGE_PATH,paragraph="False")
res = ""
for i in result:
        print(i)
        for j in i:
            temp = str(j).replace(" ",'')
            if temp.isnumeric() and len(temp) == 12:
                  res = temp
                  break
            
print("result"+res)