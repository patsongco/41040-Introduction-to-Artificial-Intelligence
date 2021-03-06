#### 41040 Introduction to Artificial Intelligence
### Assessment 2: Mini Project
# Implementation of YOLOv3 trained on MSCOCO dataset + GUI for inference
- Feature Extraction
- Object Detection
- Localization
- Classification

## How to use on the command line
**1.** Navigate to the directory you wish to clone the repo into

**2.** Clone repo with code below
```
$ git clone https://github.com/patsongco/41040-Introduction-to-Artificial-Intelligence
```

A folder named "41040-Introduction-to-Artificial-Intelligence" should be created with all the required files (exccept pre-trained Yolo_v3 weights, next step)

**3.** Download pre-trained Yolo_v3 weights [here](https://pjreddie.com/media/files/yolov3.weights) (237 MB) (*this may take several minutes depending on your internet connection*) and place file in "41040-Introduction-to-Artificial-Intelligence" folder 

**4.** Navigate to "41040-Introduction-to-Artificial-Intelligence" directory and change permissions so the yolo3 file is executable
```
$ cd 41040-Introduction-to-Artificial-Intelligence/
$ chmod +x yolo3
```
**5.** Execute GUI.py using python
```
$ python3 GUI.py
```
**6.** Window with Graphical User Interface (GUI) will apprear

![Image of GUI1](/GUI_1.png)

**7.** Click on "Choose Image" button to choose a picture from your PC. Some sample images can be found in "41040-Introduction-to-Artificial-Intelligence/data"

![Image of GUI2](/GUI_2.png)

**8.** Click on "Classify Image" button to view results (this may take several seconds depending on hardware)

![Image of GUI3](/GUI_3.png)

**9.** Repeat Steps 7 and 8 if you want to make an inference on more images
