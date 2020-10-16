#### 41040 Introduction to Artificial Intelligence
### Assessment 2: Mini Project
# Implementation of YOLOv3 trained on MSCOCO dataset + GUI for inference
- Feature Extraction
- Object Detection
- Localization
- Classification

## How to use on the command line
**1.** Navigate to the folder you wish to clone the repo

**2.** Clone repo with code below
```
$ git clone https://github.com/patsongco/41040-Introduction-to-Artificial-Intelligence
```

A folder named "41040-Introduction-to-Artificial-Intelligence" should be created with all the required files (exccept pre-trained Yolo_v3 weights: Step 4)

**3.** Change permissions so the yolo3 file is executable
```
$ chmod +x yolo3
```
**4.** Download pre-trained Yolo_v3 weights [here](https://pjreddie.com/media/files/yolov3.weights) (237 MB) and place file in "41040-Introduction-to-Artificial-Intelligence" folder

**5.** Execute GUI.py using python
```
$ python3 GUI.py
```
**6.** Window with Graphical User Interface (GUI) will apprear

![Image of GUI1](/GUI_1.png)

**7.** Click on "Choose Image" button to choose a picture for inference

![Image of GUI2](/GUI_2.png)

**8.** Click on "Classify Image" button to view results

![Image of GUI3](/GUI_3.png)

