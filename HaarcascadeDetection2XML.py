import xml.etree.ElementTree as ET
from cv2 import cv2
import os

DIR_NAME = 'datasetNew/'
path = os.getcwd()
pathDataSet = path + (r'\dataset')
algorithm = cv2.CascadeClassifier(os.path.join(
    path, 'haarcascade_frontalface_default.xml'))
data = os.listdir(pathDataSet)


def readData(data):
    count = 1
    for i in data:
        detection(os.path.join(pathDataSet, i), count)
        count += 1


def detection(file, count):
    file = cv2.imread(file)
    model = algorithm.detectMultiScale(file, scaleFactor=1.3, minNeighbors=3)
    for x, y, w, h in model:
        cv2.rectangle(file, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imwrite('datasetNew/' + str(count) + '.jpg', file)
    data = ET.Element('annotation')
    folder = ET.SubElement(data, 'folder')
    filename = ET.SubElement(data, 'filename')
    path = ET.SubElement(data, 'path')
    source = ET.SubElement(data, 'source')
    database = ET.SubElement(source, 'database')
    size = ET.SubElement(data, 'size')
    width = ET.SubElement(size, 'width')
    height = ET.SubElement(size, 'height')
    depth = ET.SubElement(size, 'depth')
    segmented = ET.SubElement(data, 'segmented')
    objected = ET.SubElement(data, 'object')
    name = ET.SubElement(objected, 'name')
    pose = ET.SubElement(objected, 'pose')
    truncated = ET.SubElement(objected, 'truncated')
    difficult = ET.SubElement(objected, 'difficult')
    bndbox = ET.SubElement(objected, 'bndbox')
    xmin = ET.SubElement(bndbox, 'xmin')
    ymin = ET.SubElement(bndbox, 'ymin')
    xmax = ET.SubElement(bndbox, 'xmax')
    ymax = ET.SubElement(bndbox, 'ymax')
    folder.text = 'dataset'
    filename.text = str(count) + '.jpg'
    path.text = os.getcwd() + '/dataset' + str(count) + '/' + str(count) + '.jpg'
    database.text = 'unknown'
    width.text = str(w)
    height.text = str(h)
    depth.text = '3'
    segmented.text = '0'
    name.text = 'ELVIN'
    pose.text = 'Unspecified'
    truncated.text = '0'
    difficult.text = '0'
    xmin.text = str(x)
    ymin.text = str(y)
    xmax.text = str(x+w)
    ymax.text = str(y+h)
    allData = ET.tostring(data)
    fileObject = open('/datasetNew/'+str(count)+'.xml', 'w')
    allData = str(allData)
    fileObject.write(allData)


if __name__ == "__main__":
    dirs = os.path.dirname(DIR_NAME)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    readData(data)
