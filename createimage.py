#Creating an Image
import cv2
import numpy as np
image = np.zeros((500,500, 3))
cv2.rectangle(image,(300,450), (50,350),(0,75,60) , 10 )
cv2.putText(image, "Mubin", (76,405),cv2.FONT_HERSHEY_DUPLEX,2 , (0, 230, 175) , 2)
cv2.imshow("image1.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
