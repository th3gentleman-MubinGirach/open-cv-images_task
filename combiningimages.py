import cv2 
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")
image1_resize = cv2.resize(image1,(200,200))
image2_resize = cv2.resize(image2,(200,200))
combine_horizontally = cv2.hconcat([image1_resize, image2_resize])
cv2.imshow('combinedimage',combine_horizontally)
cv2.waitKey()
cv2.destroyAllWindows()
