import config
import os
from imutils import paths
import shutil
import random

# grab the paths to all input images in the original input directory
# and shuffle them

imagePaths = list(paths.list_images(config.ORIG_INPUT_DATASET))
random.seed(42)
random.shuffle(imagePaths)

# compute the training and testing split
i = int(len(imagePaths) * config.TRAIN_SPLIT)
trainPaths = imagePaths[:i]
testPaths = imagePaths[:i]

# we'll be using part of the training data for validation
i = int(len(trainPaths) * config.VAL_SPLIT)
valPaths = trainPaths[:i]
trainPaths = trainPaths[i:]

#define dataset to be built
datasets = [
    ("training", trainPaths, config.TRAIN_PATH),
    ("validation", valPaths, config.VAL_PATH),
    ("testing", testPaths, config.TEST_PATH)
]

#loop over the datasets
for (dType, imagePaths, baseOutput) in datasets:
    print("[INFOR] building '{}' split".format(dType) )

    #if the output base output directory does not exit, create it
    if not os.path.exists(baseOutput):
        print(" [INFOR] 'creating {}' directory ".format(baseOutput))
        os.makedirs(baseOutput)

        # loop over the input image paths
        for inputPath in imagePaths:
            # extract the filename of the input image along with its
            # corresponding class label
            filename = inputPath.split(os.path.sep)[-1]
            label = inputPath.split(os.path.sep)[-2]

            # build the path to the label directory
            labelPath = os.path.sep.join([baseOutput, label])

            # if the label output directory does not exist, create it
            if not os.path.exists(labelPath):
                print("[INFO] 'creating {}' directory".format(labelPath))
                os.makedirs(labelPath)

                # construct the path to the destination image and then copy
                # the image itself
            p = os.path.sep.join([labelPath, filename])
            shutil.copy2(inputPath, p)
