from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

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