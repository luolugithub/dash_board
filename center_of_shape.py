# USAGE
# python center_of_shape.py --image shapes_and_colors.png

# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread('/home/luolu/PycharmProjects/BONC Cloudiip/result/ellipse_img732.jpg')
print("image shape:", image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 0, 255), 8)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center" + "(" + str(cX) + ", " + str(cY) + ")", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 4)

	# show the image
	# cv2.imshow("Image", image)
	# cv2.waitKey(0)
	print("circle_center: " + "(" + str(cX) + ", " + str(cY) + ")")
	cv2.imwrite('/home/luolu/PycharmProjects/BONC Cloudiip/result/img_center732.jpg', image)

