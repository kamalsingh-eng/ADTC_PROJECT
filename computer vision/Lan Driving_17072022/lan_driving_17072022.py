import cv2
import numpy as np
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture ("highway.mp4")

#center_points = []

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=100) # This is used to detect the moving object in video


while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    #print(height, width)
    
    # Extract Region of interest
    #roi = frame[200: 350,800: 1000]
    #roi = frame[340: 720,500: 800]
    #roi = frame[354: 576,500: 800] #first is y1 & y2 and 2nd x & x2
    #roi = frame[350: 750,600: 660] 
    #roi = frame[200: 400,100: 250]

    #area_1 = [(570, 400), (540, 500), (620, 500), (640, 400)] #1st is x & 2nd is y
    #area_1 = [(500, 354), (500, 570), (800, 570), (800, 354)] #1st is x & 2nd is y
    area_1 = [(510,550),(555,525),(800,550),(820,500),(625,420),(535,420)] #1st is x & 2nd is y--> For highway video
    #area_1 = [(555,725),(555,725),(700,725),(700,620),(555,620),(555,620)] #1st is x & 2nd is y
    for area in [area_1]:
        cv2.polylines(frame, [np.array(area, np.int32)], True, (15, 288, 18), 6)
   

    #pts = np.array([[583,356],[500,570],[610,315],[800,400],[690,600],[518,620]])
    #pts = np.array([[510,550],[650,525],[780,550],[800,500],[750,420],[535,420]]) #1st x & 2nd y, it is anticlock manner, start from bottom left
    pts = np.array([[510,550],[555,525],[800,550],[820,500],[625,420],[535,420]]) #1st x & 2nd y, it is anticlock manner, --> For highway video
    #pts = np.array([[555,725],[555,725],[700,725],[700,620],[555,620],[555,620]]) #1st x & 2nd y, it is anticlock manner
    
    ## (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x,y,w,h = rect
    croped = frame[y:y+h, x:x+w].copy()
    
    roi = croped
    
    ## (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    ## (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    ## (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg,bg, mask=mask)
    dst2 = bg+ dst

        
    # 1. Object Detection
    mask = object_detector.apply(dst2) #changed from frame to roi and this used for marking & see moving object rest should black
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # this is to remove the extra edges & info of white
    detections = []
    
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 1500:
            
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2) #change from frame to roi
            x, y, w, h = cv2.boundingRect(cnt)
                                  
            detections.append([x, y, w, h])
                       
            
     # 2. Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        print(boxes_ids)
        
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        
         #center_points.append((cx, cy))
        
        cv2.putText(dst2, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.circle(dst2, (cx, cy), 5, (0, 0, 255),  -1)
        cv2.rectangle(dst2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    #for pt in center_points:
        #cv2.circle(frame, pt, 5, (0, 255, 0),  -2)
        #class_name = tracker.update(detections)
        #if class_name in ["bike"]:
            #result = cv2.pointPolygonTest(np.array(area_1, np.int32), (int(cx), int(cy)), Truw) #--> Not in use
            #if result >= 0: #--> Not in use
                #cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                #cv2.circle(roi, (cx, cy), 5, (0, 0, 255),  -1)
                #cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
            
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("dst", dst)
    cv2.imshow("dst2", dst2)
    cv2.imshow("croped", croped)
    
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows() 