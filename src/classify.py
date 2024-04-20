import numpy as np
import os
import sys
import joblib 
from os.path import join, isdir, isfile
from os import listdir
import cv2 
from featureExtractor import FeatureExtractor
from imageLoader import loadBatch

def main():

    file_dir = os.path.dirname(__file__)
    intermediatePath = join(file_dir, "../intermediates")
    examplePath = join(file_dir, "../examples")
    svmPath = join(intermediatePath, "svm.pkl")
   
    # Input parameters, could be a path to an image or directory. In the case of a directory, all files in that directory will be evaluated
    # If no parameters are specified, the default example folder will be used
    inputPath = "../test"
    if isdir(inputPath):
        imagePaths = [join(inputPath, f) for f in listdir(inputPath) if f.endswith(('.png', '.jpg'))]
    else:
        imagePaths = [inputPath,]

    
    print("loading images...")
    Images = loadBatch(imagePaths)
    print("loading SVM model...")
    clf = joblib.load(svmPath)
        
    print("Extracting features, this may take a while for large collections of images...") # should probably use batches for this as well
    extractor = FeatureExtractor()
    features  = extractor.get_features(Images)

    classes = clf.best_estimator_.classes_ if hasattr(clf, "best_estimator_") else clf.classes_
    print("Predicting the Hieroglyph type...")
    prob = np.array(clf.predict_proba(features))
    top5_i = np.argsort(-prob)[:,0:1]
    top5_s = np.array([prob[row,top5_i[row]] for row, top5_i_row in enumerate(top5_i)])  
    top5_n = classes[top5_i]

    dict1={"V28":"twisted wick","N35":"water"}
    print("{:<25} ::: {}".format("image name", "top 3 best matching hieroglyphs"))
    for idx, path in enumerate(imagePaths):
        print("{:<25} --> {}".format(os.path.basename(path), top5_n[idx]))
        if top5_n[idx][0] in dict1.keys():
            print(dict1[top5_n[idx][0]])   





cap = cv2.VideoCapture(0)
rect_width = 75
rect_height = 100
rect_x, rect_y = 0, 0


def on_mouse_click(event, x, y, flags, param):
    global rect_x, rect_y
    if event == cv2.EVENT_LBUTTONDOWN:
        rect_x = x - rect_width // 2
        rect_y = y - rect_height // 2
        
        # Crop the frame based on the rectangle coordinates
        cropped_frame = frame[rect_y:rect_y+rect_height, rect_x:rect_x+rect_width]
        grayscale_image = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)
        # Specify the folder where you want to save the cropped image
        save_folder = "../test"  # Change this to your desired folder path
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        
        # Save the cropped image with a unique filename
        filename = "cropped_image.png"  # Change this to your desired filename
        cv2.imwrite(join(save_folder, filename), grayscale_image)
        print("Cropped image saved successfully!")


cv2.namedWindow('Video Capture')
cv2.setMouseCallback('Video Capture', on_mouse_click)

while True:
    
    ret, frame = cap.read()

    rectangle = cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (255, 0, 0), 2)

    cv2.imshow('Video Capture', rectangle)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break


cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
