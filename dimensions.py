import  cv2
img=cv2.imread('image12.jpeg')
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print('original image shape:', img.shape)
cv2.imshow('input image', img)
cv2.imshow('output image', gimg)
height = img.shape[0]
width = img.shape[1]
depth = img.shape[2]
print("height:",height)
print("width:",width)
print("depth:",depth)

cv2.waitKey()
cv2.destroyAllWindows()


