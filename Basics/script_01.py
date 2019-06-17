import cv2

img = cv2.imread('mee.png', 0) # flag can be 0, 1, -1 == grayscale, color, original
print(img) # if the images DNE, img will be None

if img == None:
	print("We messed up")
