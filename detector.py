import cv2

# Loading ClassFile, Config and Model
with open('yolofiles/coco.names') as classfile:
    classes = classfile.read().splitlines()

yoloConfigFile = 'yolofiles/yolov4.cfg'
yoloModelFile = 'yolofiles/yolov4.weights'
yoloSize = (416,416)

# Loading Darknet Configs and Setting up Framework 
darknet = cv2.dnn.readNetFromDarknet(yoloConfigFile,yoloModelFile)
detectionModel = cv2.dnn_DetectionModel(darknet)
detectionModel.setInputParams(scale=1 / 255, size=yoloSize, swapRB=True)


# Detection
def detect_objects(inputfilename):
    inputimg = cv2.imread(inputfilename)
    classIds, scores, boxes = detectionModel.detect(inputimg,confThreshold=0.6, nmsThreshold=0.4)
    object_list = []
    for (classId, score, box) in zip(classIds, scores, boxes): 
        text = (classes[classId[0]])
        object_list.append(text)
    return(object_list)


