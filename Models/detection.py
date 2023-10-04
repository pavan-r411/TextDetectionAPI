import easyocr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Image
import cv2

def identify(IMAGE_PATH):
    reader = easyocr.Reader(['en'])
    # IMAGE_PATH = 'C:\\Users\\I569380\\Documents\\VSProj\\DecisionAPI\\Models\\card.jpg'
    prediction = reader.readtext(IMAGE_PATH,paragraph="False")
    idCardNumber = ""
    for i in prediction:
    # print(i)
        for j in i:
            current_str = str(j).replace(" ",'')
            if current_str.isnumeric() and len(current_str) == 12:
                  idCardNumber = current_str
                  break

    return idCardNumber