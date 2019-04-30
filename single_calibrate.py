# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:15:03 2019

@author: TOMATO
"""

import numpy as np
import cv2
#import glob

ROWS=8
COLUMNS=11


if __name__=="__main__":
    
    objpoints=[]
    imgpoints=[]
    
    #准备标定数据，生成世界坐标系下的点，只是对应坐标，如
    #(0,0,0),(1,0,0),(2,0,0),...(6,7,0),
    objp=np.zeros((ROWS*COLUMNS,3),np.float32)
    objp[:,:2]=np.mgrid[0:ROWS,0:COLUMNS].T.reshape(-1,2)
#    objp[:,:2]=np.mgrid[0:175:8j,0:250:11j].T.reshape(-1,2)
    
    img=cv2.imread("d:/python_projects/ZED_imgleft/02left.png",-1)
    h,w,c=img.shape
#    img=cv2.imread("d:/python_projects/ZED_imgright/31right.png",-1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    ret,corners=cv2.findChessboardCorners(gray,(ROWS,COLUMNS),None)
    if ret==True:
        #使用subPix增加点的准确度
        criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
        corners_sp=cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        corners_img=cv2.drawChessboardCorners(img,(ROWS,COLUMNS),corners_sp,ret)
    
        cv2.namedWindow("corners_img",0)
        cv2.imshow("corners_img",corners_img)
        cv2.waitKey(0)
        
        objpoints.append(objp)
        imgpoints.append(corners_sp)


        
    ret,mtx,distcoeffs,rvecs,tvecs=cv2.calibrateCamera(objpoints,imgpoints,gray.shape[::-1],None,None)
#    cv2.stereoCalibrate
#    cv2.stereoRectify
    print('mtx=\n',mtx,'\ndist=',distcoeffs)
    
    
    newcameramtx,roi=cv2.getOptimalNewCameraMatrix(mtx,distcoeffs,(w,h),1,(w,h))
    
    undistort_img=cv2.undistort(img,mtx,distcoeffs,None,newcameramtx)
    
    cv2.namedWindow("undistort_img",0)
    cv2.imshow("undistort_img",undistort_img)
    cv2.waitKey(0)
    
    
    
    
    cv2.destroyAllWindows()