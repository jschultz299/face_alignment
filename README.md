# face_alignment
Code for implementing facial key point detection from Adrian Bulat's [face-alignment](https://github.com/1adrianb/face-alignment) repo.

Scritps:
   - singleImage.py
        - Performs face alignment on single image
   - camera_test.py
        - Simple test to check camera works.
        - To find camera, run ```bash
ffplay /dev/video0.py
```
   - realtime_test.py
        - Performs face alignment on live video feed
   - realtime_ros.py
        - Performs face alignment on subscribed camera topic and publishes to ROS
   - raf_fa.py
        - Code for robot-assisted feeding study
