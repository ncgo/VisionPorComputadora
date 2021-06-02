from flask import Flask, render_template, request, Response, redirect, url_for
from camera import VideoCamera
import pyzbar.pyzbar as pyzbar 
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jsglue import JSGlue
import os
import time
import json
import logging
import sys

app = Flask(__name__)
jsglue = JSGlue(app)

image = None

api = Api(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        global image
        frame, image = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

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