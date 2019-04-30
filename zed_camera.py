# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:33:48 2019

@author: TOMATO
"""

import pyzed.sl as sl
import cv2

if __name__=="__main__":
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
#    init_params.sdk_verbose = False
    # Use HD1080 video mode
    init_params.camera_resolution = sl.RESOLUTION.RESOLUTION_HD1080  
#    init_params.camera_fps = 60  # Set fps at 30
    
    init_params.sdk_gpu_id=0#default'-1',best device found
    
    # Open the camera
    err = zed.open(init_params)
    print("err info:",err)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Get camera information (ZED serial number)
#    zed_serial = zed.get_camera_information().serial_number
#    print("Hello! This is my serial number: {0}".format(zed_serial))
    #设置曝光时间/亮度等参数
    zed.set_camera_settings(sl.CAMERA_SETTINGS.CAMERA_SETTINGS_BRIGHTNESS,5,False)#,BRIGHTNESS[0,8]
#    zed.set_camera_settings(sl.CAMERA_SETTINGS.CAMERA_SETTINGS_EXPOSURE,150,False)#BRIGHTNESS,EXPOSURE
    
    image_left = sl.Mat()
    image_right = sl.Mat()
    
    runtime_parameters = sl.RuntimeParameters()
    cv2.namedWindow("left_live",0)
    cv2.namedWindow("right_live",0)
    while True:
    # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns SUCCESS
            zed.retrieve_image(image_left, sl.VIEW.VIEW_LEFT)
            
            zed.retrieve_image(image_right, sl.VIEW.VIEW_RIGHT)

            # Get the timestamp at the time the image was captured
#            timestamp = zed.get_timestamp(sl.TIME_REFERENCE.TIME_REFERENCE_CURRENT)  
#            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(
#                    image.get_width(), image.get_height(),
#                  timestamp))
            img_leftdata=image_left.get_data()
            img_rightdata=image_right.get_data()
            cv2.imshow("left_live",img_leftdata)
            cv2.imshow("right_live",img_rightdata)
            c=cv2.waitKey(1)&0xFF
            if c==27 or c==113:
                break
            
        
        
        
    print (img_leftdata.shape)













    cv2.destroyAllWindows()
    # Close the camera
    zed.close()
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
