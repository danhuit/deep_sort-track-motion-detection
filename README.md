# Re-trained yolov3
### 1. **Get source [1]**
- <p>git clone https://github.com/AlexeyAB/darknet.git<p>
- [Compile on Linux](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make) use make.
### 2. **Prepare your lable data**
- Use [lable tool](https://github.com/tzutalin/labelImg)[2]
- Save YOLO format. 
### 3. **Prepare your data**
- cd darknet
- Put your training data in folder: data/images_train.
- Put your evaluation data in fofder: data/images_eval.
- Download [pretrained convolutional weights](https://pjreddie.com/darknet/yolo/) from[3]
  - Or run script:
  <p>wget https://pjreddie.com/media/files/darknet53.conv.74<p>
- In folder darknet: make file yolo.data, yolo.names,  train.txt, test.txt
  - yolo.data
      >classes= 80
      
      >train  = train.txt
      
      >valid  = test.txt
      
      >names = yolo.names
      
      >backup = backup/
  - train.txt
    - path to your images train: 
        - data/images_train/image_1.jpg
        - data/images_train/image_n.jpg
  - test.txt
    - path to your images evaluation: 
        - data/images_train/image_1.jpg
        - data/images_train/image_n.jpg
  - yolo.names: list class name
    - person
    - dog
    - ...
### 4. **Train your data**
- Run script: ./darknet detector train yolo.data darknet53.conv.74
- **Options**
  - Multigpu: add **-gpus 0,1,2,3** after script train.
  - Save training log use:  **> train_log.txt** after script train.
    
### 3 References
- [1]  Yolov3 AlexeyAB.
- [2]  Tzutalin. LabelImg
- [3]  Redmon, Joseph and Farhadi, Ali YOLO: Real-Time Object Detection

     

   
 