import cv2, numpy

dots=cv2.imread("dots.png")

# Set our filtering parameters 
# Initialize parameter settiing using cv2.SimpleBlobDetector

params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=100
params.filterByCircularity=True
params.minCircularity=0.1
params.filterByInertia=True
params.minInertiaRatio=0.1

detection=cv2.SimpleBlobDetector_create(params)
circles=detection.detect(dots)
print(circles)
blobs=cv2.drawKeypoints(dots,circles,numpy.array((1,1)),(200,250,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#Count nber of circles
length=len(circles)
print(length)
cv2.putText(blobs,"Detected:"+str(length),(20,560),cv2.FONT_ITALIC, 1, (200,250,0), 2)
cv2.imshow("Params", blobs)

cv2.waitKey(0)
cv2.destroyAllWindows()