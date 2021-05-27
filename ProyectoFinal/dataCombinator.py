"""
Programa para el combinado de datos del dataset Fruits-360
de Kaggle para el proyecto final.

Esto combina las diferentes carpetas de las frutas en el dataset original
de acuerdo a las frutas permitidas para posteriormente ser recortado o augmentado

Escrito por Jesús Omar Cuenca Espino 
A01378844@itesm.mx

26/05/2021
"""

import os
from shutil import move, rmtree

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

filterFiles = lambda x : os.path.isfile(x)
filterDirs  = lambda x : os.path.isdir(x)

def joinDirsHelper(trainTest : str, fatherDir : str, children : list):
    os.chdir(trainTest)
    if not os.path.exists(fatherDir):
        os.makedirs(fatherDir)
    else:
        os.chdir("..")
        return None
    counter = 1
    for child in children:
        files = list(filter(lambda x : filterFiles(f"{child}/{x}"), os.listdir(child)))
        for f in files:
            termination = f.split('.')[-1]
            move(f"{child}/{f}",f"{fatherDir}/{hex(counter)[2:]}.{termination}")
            counter += 1
        rmtree(child)

    print(f"Files moved\t{counter}")

    os.chdir("..")

def joinDirs(father : str, children : list):
    assert os.path.isdir("data")
    os.chdir("data")
    print(f"Joining dir {father} in Training")
    joinDirsHelper(TRAIN_PATH,father,children)
    print(f"Joining dir {father} in Testing")
    joinDirsHelper(TEST_PATH,father,children)
    os.chdir("..")

if __name__ == "__main__":
    assert os.path.isdir("data")
    os.chdir("data")

    fruitNames = list(filter(lambda x : filterDirs(f"{TRAIN_PATH}{x}"), os.listdir(TRAIN_PATH)))

    useless = []

    filteredMap = {}

    for aF in ALLOWED_FRUITS:
        filteredMap[aF] = []

    while len(fruitNames) > 0:
        fruitName = fruitNames.pop()
        allowed = False
        for aF in ALLOWED_FRUITS:
            if aF in fruitName.lower().split():
                allowed = True
                filteredMap[aF].append(fruitName)
                break
        if not allowed:
            useless.append(fruitName)

    for uselessFruit in useless:
        rmtree(TRAIN_PATH+uselessFruit)
        rmtree(TEST_PATH+uselessFruit)

    os.chdir("..")

    for filtered in filteredMap.keys():
        joinDirs(filtered, filteredMap[filtered])