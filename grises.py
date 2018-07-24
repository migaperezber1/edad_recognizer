import cv2
import random
#import os module for reading training data directories and paths
import os, sys
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np
dirs = os.listdir(".")
subject_dir_path=os.getcwd()
l=0
for dirr in dirs:
	if dirr[-3:]!=".py": 
        
        
            #build image path
            #sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + dirr            
            #read image
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(str(l)+(".jpg"),gray)
            l+=1
            print(l)
