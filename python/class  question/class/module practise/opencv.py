import cv2

image = cv2.imread("photo.jpeg")
cv2.imshow("practice image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
print(cv2._version_)
print(image.shape)
height,width,channel = image.shape
print(width,channel,height)


#accessing pixels through index

print(image[100,200])

#it will give pixel of 100th  row and 200th column

image[100,200]=[255,0,0]#pixel value change


# converting into grayscale(combinin BGR into one value(intensity) rangin between 0-> black to 255 ->white )

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray)








"""import cv2

#image = cv2.imread("photo.JPG")
image = cv2.imread("")
if image is None:
	print("IMage not found")

else:
	cv2.imshow("practice image", image)
	cv2.waitKey(15000)

	cv2.destroyAllWindows()
	print(cv2._version_)
    """