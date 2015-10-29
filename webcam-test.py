import cv2
import cv2.cv as cv
import numpy
import zbar

cv.NamedWindow("w1", cv.CV_WINDOW_NORMAL)

camera_index = -1
capture = cv.CreateCameraCapture(camera_index)

while True:
    frame = cv.QueryFrame(capture)

    aframe = numpy.asarray(frame[:,:])
    g = cv.fromarray(aframe)
    g = numpy.asarray(g)

    imgray = cv2.cvtColor(g,cv2.COLOR_BGR2GRAY)
  
    raw = str(imgray.data)
    scanner = zbar.ImageScanner()

    scanner.parse_config('enable')          

    imageZbar = zbar.Image( frame.width, frame.height,'Y800', raw)
    scanner.scan(imageZbar)

    for symbol in imageZbar:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data          
  

    cv2.imshow("w1", aframe)

    c = cv.WaitKey(5)

    if c == 110: #if the 'n' key is pressed, the window will close and the program will exit
        exit()
