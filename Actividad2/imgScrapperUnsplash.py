"""
Escrito por Jesús Omar Cuenca Espino 
A01378844@itesm.mx

26/03/2021
"""
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from fileManager import createFolder,deleteFolder

WEBSITE_URL = "https://unsplash.com"
imgURL = []

def getURLs(images):
    for img in images:
        sources = img.get_attribute("srcset").split(" ")
        for src in sources:
            if("http" in src and "fit=crop&w=700" in src):
                imgURL.append(src)

def cleanDuplicates():
    global imgURL
    imgURL = list(dict.fromkeys(imgURL))

def writeImgs(urls : list, trainPath : str, testPath : str):
    targetFolder = trainPath
    for x in range(len(urls)):
        if(x > len(urls) * 0.8):
            targetFolder = testPath
        webImg = requests.get(urls[x])
        f = open(f"./{targetFolder}img_{x}.png","wb")
        f.write(webImg.content)
        f.close()

def mainActivity(driver, currentHeight, targetNumImgs):
    global imgURL
    # Get scroll height
    last_height = currentHeight
    new_height  = -1
    iters = 0
    toBottom = False
    while len(imgURL) < targetNumImgs and iters < 20:
        # Wait to load page
        time.sleep(1)

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*31/33);" if toBottom else "window.scrollTo(0, document.body.scrollHeight*9/11);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        images = driver.find_elements_by_class_name("_2UpQX")

        getURLs(images)
        cleanDuplicates()

        iters += 1

        if new_height == last_height:
            print("Height didn't update")
            if(toBottom):
                break
            else:
                toBottom = True
        last_height = new_height


if __name__ == "__main__":
    openBrowser = True
    try:
        pathFile = open("pathFile.txt","r")
        driver = Chrome(pathFile.readline())
        pathFile.close()
        driver.get(WEBSITE_URL)
        searchBar = driver.find_element_by_name("searchKeyword")
    except Exception:
        openBrowser = False

    keyword = ""

    try:
        if not openBrowser:
            raise Exception("No path to the selenium web driver")
        keyword = sys.argv[1]
        searchBar.send_keys(keyword)
        searchBar.send_keys(Keys.ENTER)
    except IndexError:
        openBrowser = False
        driver.close()

    targetNumImgs = -1

    try:
        targetNumImgs = int(sys.argv[2])
    except IndexError:
        targetNumImgs = 100

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    if(openBrowser):

        trainFolder = f"train/{keyword}/"
        testFolder  = f"test/{keyword}/"

        deleteFolder(trainFolder)
        deleteFolder(testFolder)
        
        mainActivity(driver, last_height, targetNumImgs)

        driver.close()

        createFolder(trainFolder)
        createFolder(testFolder)

        writeImgs(imgURL,trainFolder,testFolder)