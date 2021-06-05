import cv2, numpy as np
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

cv2.imshow("image1", image1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("image2", image2)
cv2.waitKey()
cv2.destroyAllWindows()

image1_crop = image1[150:470,150:520]
image2[150:470,150:520] = image1_crop
cv2.imshow("new",image2)
cv2.waitKey()
cv2.destroyAllWindows()

image2 = cv2.imread("image2.jpg")
image2_crop = image2[150:470,150:520]
image1[150:470,150:520] = image2_crop
cv2.imshow("new",image1)
cv2.waitKey()
cv2.destroyAllWindows()
