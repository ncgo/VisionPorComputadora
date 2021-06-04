from flask import Flask, render_template, request, Response, redirect, url_for
from camera import VideoCamera
from DarknetNetwork.darknet_module import set_bounding_boxes
import pyzbar.pyzbar as pyzbar 
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jsglue import JSGlue
import os
import time
import json
import logging
import numpy as np
import sys
from PIL import Image
import base64
import io

app = Flask(__name__)
jsglue = JSGlue(app)
image = None
frame = None
api = Api(app)
capture = True
CORS(app)


@app.route('/')
def index():
    capture = True
    return render_template('index.html')

def tagFormatter(detections):
    if len(detections) < 1:
        return "Found nothing"
    return detections[0][0]


## For the love of god, do not erase
# def renderImg():
#     global capture
#     capture = False
#     labels = set_bounding_boxes(image)
#     print(labels)
#     im = Image.fromarray(image)
#     data = io.BytesIO()
#     im.save(data, "JPEG")
#     encoded_img_data = base64.b64encode(data.getvalue())
#     capture=True
#     return render_template(
#         "renderCapture.html", 
#         captured_img=encoded_img_data.decode('utf-8'),
#         labels=tagFormatter(labels)
#     )

@app.route('/capture')
def renderImg():
    global capture
    capture = False
    labels = set_bounding_boxes(image)
    im = Image.fromarray(image)
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    capture=True
    return render_template(
        "renderCapture.html", 
        captured_img=encoded_img_data.decode('utf-8'),
        labels=tagFormatter(labels)
    )

def gen(camera):
    while True and capture:
        global image, frame
        frame, image = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    if capture :
        return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    return "none"

# class index(Resource):
#     def get(self):
#         return render_template('index.html')

"""
class Similarity(Resource):
    def get(self, user1, user2):
        sim_cats = main.GetSimilarity(user1, user2)
        return {"categories": sim_cats}
"""

# api.add_resource(index, '/')

#api.add_resource(Similarity, '/similarity/<string:user1>/<string:user2>')

if __name__ == '__main__':
    app.run(debug=True)