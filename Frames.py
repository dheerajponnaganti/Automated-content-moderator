import cv2
import numpy as np
import os


cam = cv2.VideoCapture("output.mp4")

try: 
      
    
    if not os.path.exists('Extracted_frames'): 
        os.makedirs('Extracted_frames') 
  

except OSError: 
    print ('Error: Creating directory of data') 
  

currentframe = 0
count1 = 1



while(True): 
      
    
    ret,frame = cam.read() 
  
    if ret: 
         
        name = './Extracted_frames/frame' + str(currentframe) + '.jpg'
        #print ('Creating...' + name) 
  
        
        if currentframe % 6 == 0:
            cv2.imwrite(name, frame) 
            count1 += 1
 
        currentframe += 1
    else: 
        break
  
cam.release() 
cv2.destroyAllWindows()
