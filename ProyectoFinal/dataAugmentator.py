"""
Programa de Apoyo para la augmentacion de datos 
del proyecto usando la libreria de TensorFlow

hecho por Jesús Omar Cuenca Espino 

27/05/2021
"""

import os
import tensorflow as tf
import numpy as np
from random import shuffle
from dataclasses import dataclass
from tensorflow.keras import layers


IMG_SIZE = 180
MAX_TESTING  = 300
MAX_TRAINING = 3000

TRAIN_PATH      = "train/"
TEST_PATH       = "test/"
VALIDATION_PATH = "validation/"

ALLOWED_FRUITS = [
    "tomato",
    "peach",
    "apple",
    "banana",
    "potato",
    "eggplant",
    "pear",
    "lemon",
    "plum",
    "avocado", # 10
    "grape",
    "watermelon",
    "onion",
    "mango",
    "cantaloupe",
    "pepper",
    "cherry",
    "orange",
    "cucumber",
    "strawberry" # 20 
]

@dataclass(frozen=True, order=True)
class Data:
    train   : int
    test    : int

@dataclass(order=True)
class FruitInfo:
    """
    Fruit info data structure
    """
    name        : str
    stats       : Data
    trainSet    : list
    testingSet  : list

data_augmentation = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
  layers.experimental.preprocessing.RandomRotation(0.2),
])

def augmentImgs(path : str, name : str) -> list:
    img = tf.keras.preprocessing.image.load_img(path+name, target_size=(IMG_SIZE,IMG_SIZE))
    pix = np.array(img)
    pix = tf.expand_dims(pix, 0)
    newFileNames = []
    for i in range(9):
        fileName = f"AugmentedImg.{i}.{name}"
        newFileNames.append(fileName)
        augmented_image = data_augmentation(pix)
        tf.keras.preprocessing.image.save_img(path+fileName, augmented_image[0])
    return newFileNames

def deleteExtraFiles(path : str, files : list):
    for f in files:
        os.remove(path+f)

def standardizeHelper(path : str, limit : int, files : list):
    filesCopy   = list(files)
    shuffle(filesCopy)
    extraFiles  = []

    ## Augmentation of data
    counter = 0
    while len(filesCopy) + len(extraFiles) < limit:
        extraFiles.extend(augmentImgs(path,filesCopy[counter]))
        counter += 1
    filesCopy.extend(extraFiles)

    ## Remove extra files that are beyond the limit
    if len(filesCopy) > limit:
        filesToRemove = filesCopy[limit:]
        deleteExtraFiles(path, filesToRemove)
        filesCopy = filesCopy[:limit]

    return filesCopy

def standardizeNumbers(fruits : dict):
    for fruit in fruits.keys():
        trainingSet = standardizeHelper(f"data/{TRAIN_PATH}{fruit}/",MAX_TRAINING,   fruits[fruit].trainSet)
        testingSet  = standardizeHelper(f"data/{TEST_PATH}{fruit}/" ,MAX_TESTING,    fruits[fruit].testingSet)
        fruitMap[fruit] = FruitInfo(
            fruit,
            Data(
                len(trainingSet),
                len(testingSet)
            ),
            trainingSet,
            testingSet
        )
        print(fruit+"\tCompleted Standarization")

if __name__ == "__main__":
    assert os.path.isdir("data")
    os.chdir("data")

    fruitMap = {}

    for fruit in ALLOWED_FRUITS:
        trainingSet = list(filter(lambda x : os.path.isfile(f"{TRAIN_PATH}{fruit}/{x}"), [fileName for fileName in os.listdir(f"{TRAIN_PATH}{fruit}")]))
        testingSet  = list(filter(lambda x : os.path.isfile(f"{TEST_PATH}{fruit}/{x}"), [fileName for fileName in os.listdir(f"{TEST_PATH}{fruit}")]))
        result = Data(
            len(trainingSet),
            len(testingSet)
        )
        fruitMap[fruit] = FruitInfo(fruit,result,trainingSet,testingSet)

    os.chdir("..")

    standardizeNumbers(fruitMap)